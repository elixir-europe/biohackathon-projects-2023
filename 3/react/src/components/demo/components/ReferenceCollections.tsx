/* Import Dependencies */
import classNames from 'classnames';
import { Row, Col } from 'react-bootstrap';

/* Import Types */
import { VirtualReferenceCollection } from 'app/types/VirtualReferenceCollection';

/* Import Styles */
import styles from 'components/demo/demo.module.scss';


/* Props Typing */
interface Props {
    virtualReferenceCollection: VirtualReferenceCollection | undefined
}


const ReferenceCollections = (props: Props) => {
    const { virtualReferenceCollection } = props;

    return (
        <Row className="h-100">
            <Col>
                <div className={`${styles.referenceCollectionsBlock} h-100`}>
                    {/* Render the different taxas */}
                    {virtualReferenceCollection?.taxa?.map((taxon, index) => {
                        return (
                            <Row key={taxon.taxonID} className={`${index > 0 && 'mt-4'}`}>
                                <Col>
                                    <div className={`${styles.referenceCollectionBlock} d-flex flex-column overflow-hidden px-3 py-3`}>
                                        <p className="fs-2 fw-lightBold p-0 m-0"> {taxon.taxonName?.taxonFullName} </p>

                                        {/* Render the different organisms */}
                                        <div className="flex-grow-1 overflow-hidden">
                                            {taxon.organisms?.map((organism) => {
                                                return (
                                                    <Row className="h-100">
                                                        <Col className="h-100 d-flex flex-column">
                                                            <p className="fs-3"> {organism.organismID} </p>

                                                            {/* Render the different occurrences with their media */}
                                                            <div className="flex-grow-1 overflow-hidden">
                                                                {organism.occurrences?.map((occurrence) => {
                                                                    return (
                                                                        <>
                                                                            {/* Indicator for occurrence */}
                                                                            <Row className="h-100">
                                                                                {/* Render different media items */}
                                                                                {occurrence.media?.map((mediaItem) => {
                                                                                    return (
                                                                                        <Col md={{ span: 4 }}
                                                                                            className="h-100 px-3"
                                                                                        >
                                                                                            <div
                                                                                                className={`${styles.referenceImage} d-flex justify-content-center bgc-grey h-100 w-100 overflow-hidden`}
                                                                                            >
                                                                                                <img src={mediaItem.mediaDataURL}
                                                                                                    alt={mediaItem.mediaID}
                                                                                                    className={"h-100"}
                                                                                                />
                                                                                            </div>
                                                                                        </Col>
                                                                                    );
                                                                                })}
                                                                            </Row>
                                                                        </>
                                                                    );
                                                                })}
                                                            </div>
                                                        </Col>
                                                    </Row>
                                                );
                                            })}
                                        </div>
                                    </div>
                                </Col>
                            </Row>
                        );
                    })}
                </div>
            </Col>
        </Row>
    );
}

export default ReferenceCollections;
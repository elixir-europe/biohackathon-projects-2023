/* Import Dependencies */
import { useState } from 'react';
import { Container, Row, Col } from 'react-bootstrap';

/* Import Types */
import { VirtualReferenceCollection } from 'app/types/VirtualReferenceCollection';

/* Import Styles */
import styles from './demo.module.scss';

/* Import API */
import GetVirtualReferenceCollection from 'api/VirtualReferenceCollection/GetVirtualReferenceCollection';

/* Import Components */
import Header from 'components/general/header/Header';
import Information from './components/Information';
import Instruction from './components/Instruction';
import Dropdown from './components/Dropdown';
import MetadataBlock from './components/MetadataBlock';
import ReferenceCollections from './components/ReferenceCollections';
import Footer from 'components/general/footer/Footer';


const Demo = () => {
    const [virtualReferenceCollection, setVirtualReferenceCollection] = useState<VirtualReferenceCollection | undefined>();

    const SelectReferenceCollection = (referenceCollectionID: string) => {
        GetVirtualReferenceCollection(referenceCollectionID).then((virtualReferenceCollection: VirtualReferenceCollection) => {
            if (Object.keys(virtualReferenceCollection)) {
                setVirtualReferenceCollection(virtualReferenceCollection);
            }
        }).catch(error => {
            console.warn(error);
        });
    }

    return (
        <div className="h-100 d-flex flex-column">
            <Header />

            <Container fluid className="flex-grow-1 overflow-hidden pt-5 pb-4">
                <Row className="h-100">
                    <Col md={{ span: 10, offset: 1 }} className="h-100">
                        <Row className="h-100">
                            {/* Demo information */}
                            <Col md={{ span: 4 }} className="d-flex flex-column h-100">
                                <div>
                                    <Instruction />
                                </div>

                                <div className="flex-grow-1 mt-4">
                                    <Information />
                                </div>
                            </Col>

                            {/* Demo reference collection */}
                            <Col md={{ span: 8 }} className="h-100 d-flex flex-column">
                                <div>
                                    <Row>
                                        <Col md={{ span: 4 }}>
                                            <Dropdown selectedOption={virtualReferenceCollection ?
                                                virtualReferenceCollection.virtualReferenceCollectionMetaData.referenceCollectionID : ''
                                            }
                                                SelectReferenceCollection={(referenceCollectionID: string) => SelectReferenceCollection(referenceCollectionID)}
                                            />
                                        </Col>
                                    </Row>
                                </div>

                                <div className={`${styles.scrollBlock} flex-grow-1 mt-4`}>
                                    {virtualReferenceCollection ?
                                        <div className="h-100 d-flex flex-column">
                                            <div className={`${styles.metadataBlock}`}>
                                                <Row>
                                                    <Col className="px-4 py-2">
                                                        <MetadataBlock virtualReferenceCollection={virtualReferenceCollection} />
                                                    </Col>
                                                </Row>
                                            </div>

                                            <div className="flex-grow-1 mt-3">
                                                <ReferenceCollections virtualReferenceCollection={virtualReferenceCollection} />
                                            </div>
                                        </div>
                                        :
                                        <div className="h-100 d-flex justify-content-center align-items-center">
                                            Please select a Virtual Reference Collection
                                        </div>
                                    }
                                </div>
                            </Col>
                        </Row>
                    </Col>
                </Row>
            </Container>

            <Footer />
        </div>
    );
}

export default Demo;
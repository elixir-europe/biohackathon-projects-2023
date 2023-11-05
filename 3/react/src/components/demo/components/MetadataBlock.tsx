/* Import Dependencies */
import { Row, Col } from 'react-bootstrap';

/* Import Types */
import { VirtualReferenceCollection } from "app/types/VirtualReferenceCollection"


/* Props Typing */
interface Props {
    virtualReferenceCollection: VirtualReferenceCollection
}


const MetadataBlock = (props: Props) => {
    const { virtualReferenceCollection } = props;

    return (
        <Row>
            <Col>
                <Row>
                    <Col>

                        <p className="fw-lightBold"> Metadata </p>
                    </Col>
                </Row>

                <Row>
                    <Col md={{ span: 8 }}>
                        <table>
                            <thead>
                                <tr>
                                    <th>
                                        Property
                                    </th>
                                    <th>
                                        Value
                                    </th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>
                                        Creator
                                    </td>
                                    <td>
                                        {virtualReferenceCollection.virtualReferenceCollectionMetaData.creator}
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        Maintainer
                                    </td>
                                    <td>
                                        {virtualReferenceCollection.virtualReferenceCollectionMetaData.maintainer}
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        Title
                                    </td>
                                    <td>
                                        {virtualReferenceCollection.virtualReferenceCollectionMetaData.title}
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        Description
                                    </td>
                                    <td>
                                        {virtualReferenceCollection.virtualReferenceCollectionMetaData.description}
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        Taxa Included Description
                                    </td>
                                    <td>
                                        {virtualReferenceCollection.virtualReferenceCollectionMetaData.area?.toString()}
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </Col>
                    <Col md={{ span: 4 }}>
                        <table>
                            <thead>
                                <tr>
                                    <th>
                                        Property
                                    </th>
                                    <th>
                                        Value
                                    </th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>
                                        Copyright License
                                    </td>
                                    <td>
                                        {virtualReferenceCollection.virtualReferenceCollectionMetaData.copyrightLicense}
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        Copyright Owner
                                    </td>
                                    <td>
                                        {virtualReferenceCollection.virtualReferenceCollectionMetaData.copyrightOwner}
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        Area
                                    </td>
                                    <td>
                                        {virtualReferenceCollection.virtualReferenceCollectionMetaData.area?.toString()}
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        Language
                                    </td>
                                    <td>
                                        {virtualReferenceCollection.virtualReferenceCollectionMetaData.language}
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        Last Updated
                                    </td>
                                    <td>
                                        {virtualReferenceCollection.virtualReferenceCollectionMetaData.lastUpdate}
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </Col>
                </Row>
            </Col>
        </Row>
    );
}

export default MetadataBlock;
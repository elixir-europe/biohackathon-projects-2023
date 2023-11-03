/* Import Dependencies */
import { Row, Col } from 'react-bootstrap';


const Instruction = () => {
    return (
        <Row className="h-100">
            <Col className="h-100">
                <div className="bgc-secondary px-4 py-3 h-100">
                    <p className="fs-4">
                        <span className="fw-lightBold">The demo:</span> select a reference collecton from the list.
                        It will display the metadata and all of the occurrences, with attached media, that can
                        be used for refferencing.
                    </p>
                </div>
            </Col>
        </Row>
    );
}

export default Instruction;
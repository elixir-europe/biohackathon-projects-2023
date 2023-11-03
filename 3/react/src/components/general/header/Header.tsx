/* Import Components */
import { Container, Row, Col } from 'react-bootstrap';


const Header = () => {
    return (
        <Container fluid className="bgc-primary py-3">
            <Row>
                <Col md={{ span: 10, offset: 1 }}>
                    <h1> Virtual Reference Collection </h1>
                </Col>
            </Row>
        </Container>
    );
}

export default Header;
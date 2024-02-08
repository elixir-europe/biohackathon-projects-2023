/* Import Dependencies */
import { Container, Row, Col } from 'react-bootstrap';


const Footer = () => {
    return (
        <Container fluid>
            <Row>
                <Col md={{ span: 10, offset: 1 }}>
                    <p> Elixir Biohackathon 2023 </p>
                </Col>
            </Row>
        </Container>
    );
}

export default Footer;
/* Import Dependencies */
import { Row, Col } from 'react-bootstrap';


const Information = () => {
    return (
        <Row className="h-100">
            <Col className="h-100">
                <div className="bgc-secondary px-4 py-3 h-100">
                    <p className="fs-4">
                        We are proud to present our project, "Building a Virtual Reference Collection for Bumblebees (Bombus),"
                        developed during the BioHackathon 2023 of Elixir Europe. This project, represented as "Project 3: Automating
                        the building of a virtual, distributed pollinator reference collection," aims to develop a linked open data
                        schema that enhances the accessibility, organization, and utilization of taxonomic information for pollinators,
                        particularly focusing on Bumblebees.
                    </p>
                    <p className="fs-4">
                        We have developed a virtual reference collection to address the challenge of insufficient data for European bee species,
                        potentially revealing more at-risk species and aiding naturalists and researchers. Our project aims to expand species
                        identification tools to improve pollinator observations, fostering large-scale collaboration and citizen science for the
                        identification and preservation of these crucial species.
                    </p>
                    <p className="fs-4">
                        Our demo schema, using the JSON data-interchange format and linked to databases like GBIF and Fauna Europeana, serves as an
                        essential prototype for the broader "TETTRIs" project, aligning the virtual pollinator reference collection with existing data
                        standards like Darwin Core etc.
                    </p>
                    <p className="fs-4">
                        The future prospects of our virtual reference collection schema involve expanding it with additional data elements, transitioning to a
                        linked data-based approach, making it open access on platforms like GitHub, establishing connections to databases like BOLD, ENA,
                        and GloBI to facilitate informed identifications, and contributing to scientific knowledge and community engagement, ultimately serving
                        as a vital resource for pollinator conservation and biodiversity research.
                    </p>
                </div>
            </Col>
        </Row>
    );
}

export default Information;
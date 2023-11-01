# ENA upload template builder

A dockerized Vue/Flask app to simplify ENA upload form creation.
Intended to be wrapped as a Galaxy interactive tool.

## Local web app development

For development of the Flask/Vue.js app.

This assumes that you are on a Unix command line with virtualenv installed and
python>=3.10 and node.js/npm available. I am on `node==v16.20.2`, `npm==8.19.4`.

```bash
 git clone https://github.com/elixir-europe/biohackathon-projects-2023.git
 cd biohackathon-projects-2023/19/ena_template_builder/

 # Create and activate virtual environment
 virtualenv venv
 . venv/bin/activate

 # Install python dependencies
 pip install -r requirements.txt

 # Install client dependencies
 cd client/
 npm i
 cd ..

 # Run the application - this will run the client and API in parallel. The
 # client server
 honcho start
```

The application should be running at `http://localhost:5173/`.

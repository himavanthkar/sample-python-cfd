# Food Delivery API - Flask Backend Server

[![CircleCI Build Status](https://circleci.com/gh/CircleCI-Public/sample-python-cfd.svg?style=shield)](https://circleci.com/gh/CircleCI-Public/sample-python-cfd) [![Software License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/CircleCI-Public/sample-python-cfd/main/LICENSE)

## Description

**CFD (Continuous Food Delivery)** is a complete food delivery backend API built with Flask and Connexion. This is a fully functional restaurant management system that provides:

- **Menu Management**: Add, list, and retrieve restaurant menu items
- **Shopping Cart**: Session-based cart system for customers
- **Image Management**: Upload and serve food images
- **REST API**: Complete OpenAPI/Swagger specification

This project demonstrates modern Python web development practices with proper CI/CD integration using CircleCI.

## Getting Started

If you would like to copy the [config.yml](https://github.com/CircleCI-public/sample-python-cfd/blob/main/.circleci/config.yml) and adapt it to your project, be sure to read the comments in the config file to ensure it works for your project. For more details, see the [CircleCI configuration reference](https://circleci.com/docs/2.0/configuration-reference/).

## Addtional Sample Configuration Files

Inside the `.circleci` directory, you will find an `extended` directory that extends the configuration beyond the default `.circleci/config.yml`. These configuration files are tested with every pull request to this sample app, so they stay up to date and verified working.

### Heroku Deploy

The `.circleci/extended/heroku-deploy.yml` configuration file extends the default config by adding a job to deploy to heroku via a git push. For more information on how to configure this for your own project, visit the [CircleCI docs](https://circleci.com/docs/2.0/deployment-integrations/#a-simple-example-using-heroku) for more details

### Pylint

The `.circleci/extended/pylint.yml` configuration file extends the default config by adding a step to sample job. The `.pylintrc` in the project directory is configured to fail the pipeline if any errors are present when linting.

## API Features

### Core Functionality

- **Menu Items**: Create, read, update, and delete restaurant menu items
- **Shopping Cart**: Add/remove items from customer carts (session-based)
- **Image Upload**: Upload and manage food images for menu items
- **RESTful Design**: Full OpenAPI/Swagger specification with interactive documentation

### API Endpoints

- `GET /menu` - List all menu items
- `POST /menu` - Add new menu item
- `GET /menu/{itemId}` - Get specific menu item
- `GET /cart` - List cart items
- `POST /cart` - Add item to cart
- `DELETE /cart/{itemId}` - Remove item from cart
- `POST /image` - Upload food image
- `GET /image/{imageId}` - Retrieve image
- `DELETE /image/{imageId}` - Delete image

### Interactive API Documentation

When you start up the service, you can open [this page](http://localhost:8080/CFD/1.0.0/ui/) in your browser to view the interactive API documentation.

![Swagger UI Screenshot](https://raw.githubusercontent.com/CircleCI-Public/sample-python-cfd/main/.github/img/preview.png)

### Front-End Integration

This backend API is designed to work with frontend applications. For a complete food delivery experience, you can use compatible frontend projects:

| Language |  GitHub | Description |
|---|---|---|
|  Javascript (Vue.js) | [Link](https://github.com/CircleCI-Public/sample-javascript-cfd)  | Vue.js Frontend for CFD API |

## Run and Test Locally

If you would like to try this application out locally, you can find runtime instructions below.

### Requirements

Python 3.5.2+ OR Docker

### Run Local Server

To run the server on a Docker container, please execute the following from the root directory:

```bash
docker-compose up --build
```

If not using docker, to run the server, please execute the following from the root directory:

```
pip3 install -r run-requirements.txt
python3 -m openapi_server
```

### Tests

To launch the unit tests, use pytest:

```
pip3 install -r requirements.txt
pytest
```

If you want to run tests using a live database, use the alternative compose file:

```
docker-compose -f docker-compose-test.yml up --build --exit-code-from web
```

## Additional Resources

* [CircleCI Docs](https://circleci.com/docs/) - The official CircleCI Documentation website.
* [CircleCI Configuration Reference](https://circleci.com/docs/2.0/configuration-reference/#section=configuration) - From CircleCI Docs, the configuration reference page is one of the most useful pages we have.


## License

This repository is licensed under the MIT license.
The license can be found [here](./LICENSE).
# changes made

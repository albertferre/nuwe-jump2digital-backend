<a name="readme-top"></a>
<br />
<div align="center">
  <h3 align="center">Nuwe jump2digital Backend README</h3>

</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Desde el equipo de front se está creando un panel de Networking para poder filtrar una lista de empresas de forma simple y conseguir que la conexión entre empresas y usuarios sea más fluida.

Para mejorar más la experiéncia de usuario, en la versión V2 se quieren mostrar unas analíticas sobre las empresas que hay en la base de datos.

Y ahí reside el reto, en generar varios endpoints que ayuden al equipo de front a montar un panel de analíticas sin tener que tratar los datos directamente desde allí.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* Docker
* FastAPI
* Python


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Instrucciones para ejecutar el código

### Prerequisites

Para ejecutar el código se necesita tener instaldo:
* Docker
* Conda

### Installation

1. Arrancar el servidor mongodb con la instrucción:
    ```sh
    docker run -d -p 27017:27017 --name m1 mongo
    ```
2. Preparar el entorno ejecutando:
   ```sh
   conda env create -f env.yaml
   ```
3. activare el entorno
   ```sh
   conda activate nuwe-jump2digital-backend
   ```
4. Arrancar servidor API
   ```js
   uvicorn main:app --reload
   ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

Con el servidor en marcha se pueden consultar las compañías con:
* http://127.0.0.1:8000/companies
* http://127.0.0.1:8000/companies?sorted_by=founded
* http://127.0.0.1:8000/companies?sorted_by=size
* http://127.0.0.1:8000/summary


<p align="right">(<a href="#readme-top">back to top</a>)</p>
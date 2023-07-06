from fastapi import FastAPI
import uvicorn
from API.Api import Model,funcion


app=FastAPI(title='PRUEBA')

@app.post('/prueba')
def prueba(numero:Model):
    contenido=funcion(numero.tipo)
    return {
        'ENSEÑANZA':contenido[0],
        'TOKEN':contenido[1]
    }


if __name__ == '__main__':
    uvicorn.run(app=app,port=8081)

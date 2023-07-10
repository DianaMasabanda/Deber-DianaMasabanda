from pydantic import BaseModel
import openai as op

op.api_key='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'
op.organization='org-VIXUQ6yjxGQioPSLM1i12zze'

class Model(BaseModel):
    tipo : int

def funcion(frase:int)->list:
    contenido=op.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role':'system','content':
             '''Eres un profesor de programacion que enseña para la universidad
               E.G '''},
            {'role':'user','content':'La enseñanza es la siguiente'+str(frase)}
        ]


    )
    v1=contenido.choices[0].message.content
    v2=contenido.usage.total_tokens
    return [v1,v2]

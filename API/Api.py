from pydantic import BaseModel
import openai as op

op.api_key='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'
op.organization='org-Yo1JN6VlDoZBuPwiLbGxWPgm'

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
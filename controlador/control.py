from graphene import Schema
from controlador.query import Query
from controlador.mutation import Mutation

schema = Schema(query=Query, mutation=Mutation)
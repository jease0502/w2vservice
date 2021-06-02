#!/usr/bin/env python3
# coding=utf-8
# -*- coding: UTF-8 -*-
import uvicorn
from gensim.models import word2vec
import numpy as np
import pandas as pd
from fastapi import FastAPI
from fastapi.params import Form
from fastapi.responses import PlainTextResponse, RedirectResponse

# model variables

app = FastAPI(
    title="W2V Service",
    description="Web service for W2V"
)


@app.on_event("startup")
async def initial():
    global bow_model
    # Load model
    bow_model = word2vec.Word2Vec.load('./data/ckip.model.bin')


@app.get('/', include_in_schema=False)
async def index():
    return RedirectResponse('/docs')


@app.post('/', response_class=PlainTextResponse)
async def tokenize(
        sentence_list: str = Form(
            ...,
            description=r'以下使用範例單詞[閱讀]進行示範(`\n`)',
            example='閱讀'
        )
):
    global bow_model
    # Load model
    bow_model = word2vec.Word2Vec.load('./data/ckip.model.bin')

    # Show results
    get_str = bow_model.most_similar(sentence_list)
    return get_str[0][0] + '\n'

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=4088)
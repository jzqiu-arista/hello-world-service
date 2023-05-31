#!/usr/bin/env python                                                                                                                                                                        
# Copyright (c) 2023 Arista Networks, Inc.  All rights reserved.                                                                                                                             
# Arista Networks, Inc. Confidential and Proprietary.

from flask import Flask, jsonify
app = Flask(__name__)

def result( c, code=200 ):
   r = jsonify( c )
   r.status_code = code
   return r

@app.route( '/' )
def helloWorld():
   return result( 'hello world!' )

@app.route( '/health', methods=[ 'GET' ] )
def health():
   return result( { 'status': 'Alive!' } )

if __name__ == "__main__":
   app.run(debug=True)
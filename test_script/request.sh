#!/bin/bash

curl -X GET  http://localhost:8080/
curl -X GET  http://localhost:8080/test
curl -X POST http://localhost:8080/test -d 'foo=bar'
curl -X GET  http://localhost:8080/person/foo
curl -X POST http://localhost:8080/person -H "Content-Type: application/json" -d '{"id":10, "name":"foo"}'
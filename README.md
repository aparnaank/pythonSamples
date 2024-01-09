# pythonSamples

Sample Backends
GET
curl http://localhost:5000/testEP/get_request -v

POST
curl -X POST http://localhost:5000/testEP/post_request --header 'Content-Type: application/json' -d'{"type":"info" }' -v

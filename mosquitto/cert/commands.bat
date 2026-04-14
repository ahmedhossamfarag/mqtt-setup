echo Creating self-signed certificate...
openssl req -new -x509 -days 365 -extensions v3_ca -keyout ca.key -out ca.crt
openssl genrsa -aes256 -out server.key 2048
openssl req -out server.csr -key server.key -new
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt -days 365
openssl genrsa -aes256 -out client.key 2048
openssl req -out client.csr -key client.key -new
openssl x509 -req -in client.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out client.crt -days 365
@REM Use "password" as the password when prompted for the private keys.
@REM Use "localhost" as the Common Name (CN) when prompted for the server certificate.
echo Certificate created.
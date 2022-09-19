
## Run Locally


Go to the project directory

```bash
  cd <project_directory>
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server without ssl enabled

```bash
  python manage.py runserver
```

Start the server with ssl enabled

```bash
  python manage.py runsslserver --certificate cert.pem --key key.pem
```


## To generate SSL certificate you can follow this tutorial

 - [Creating an SSL certificate for localhost ](https://medium.com/@millienakiganda/creating-an-ssl-certificate-for-localhost-in-django-framework-45290d905b88)
 - [Create Locally Trusted SSL Certificates with mkcert on Windows](https://technixleo.com/create-locally-trusted-ssl-certificates-with-mkcert-on-windows/)
 - [Create Locally Trusted SSL Certificates on Linux|macOS using mkcert](https://computingforgeeks.com/create-locally-trusted-ssl-certificates-on-linux-macos-using-mkcert/)


## For setting up two factor authentication you can follow this tutorial

[Towards Django Two Factor Authentication Integration](https://www.youtube.com/watch?v=0SB9K8Dr5ck)


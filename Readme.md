### Ambiente Docker
* Django 2.2
```
cd \pydjango
sudo docker-compose up
sudo docker container ls
sudo docker-compose down
http://localhost:8000/admin

``` 
* Portainer (controle de imagens)
- admin/controle2000
```
cd \portainer
sudo docker-compose up
http://localhost:9000/

```
### Configurando acesso ao Git
```
git init
git config --global user.name "Fulano de tal"
git config --global user.email "email@gmail.com"
git pull url
git remote add origin https://github.com/plsergio/djangoApi.git

git add . (Adicionando Arquivos)
git commit -m "issue"
git push --set-upstream origin master
```



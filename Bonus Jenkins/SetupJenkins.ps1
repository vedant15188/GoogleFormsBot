docker version
docker pull jenkins/jenkins
docker run -p 8080:8080 --detach --name jenkins jenkins/jenkins
Start-Sleep -Milliseconds
docker exec -it jenkins cat /var/jenkins_home/secrets/initialAdminPassword
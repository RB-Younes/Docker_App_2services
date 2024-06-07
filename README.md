# Projet Programmation Distribuée

## Description

Ce projet, réalisé dans le cadre du Master 1 Vision Machine Intelligente à l'Université Paris Cité, a pour objectif de développer et déployer une application web en utilisant des technologies modernes. Le projet met en œuvre des conteneurs Docker, Kubernetes pour la gestion des conteneurs, PostgreSQL pour la base de données, et l'architecture de micro-services.

## Auteurs

- Abed Nada Fatima-Zahra
- Rebai Mohamed Younes
- Benmehrez Dima Sabrine

## Fonctionnalités

1. **Développement Initial et Déploiement**
    - Application Django pour une to-do list.
    - Conteneurisation avec Docker.
    - Déploiement sur un cluster Kubernetes.
    - Utilisation de PostgreSQL hébergée sur Heroku pour la gestion des données.
    - Interface de visualisation des données avec Retool.

2. **Micro-services**
    - Ajout d'une gateway et d'un deuxième service pour les prévisions météorologiques.
    - Communication entre les services pour récupérer et afficher les données météo.

## Technologies Utilisées

- **Framework Backend**: Django
- **Conteneurisation**: Docker
- **Orchestration**: Kubernetes
- **Base de Données**: PostgreSQL sur Heroku
- **Interface de Gestion**: Retool

## Instructions de Déploiement

1. **Construire l'image Docker**
    ```bash
    docker build -t front-end-app .
    ```

2. **Publier l'image Docker sur Docker Hub**
    ```bash
    docker tag front-end-app:latest yourdockerhubusername/front-end-app:latest
    docker push yourdockerhubusername/front-end-app:latest
    ```

3. **Créer un déploiement Kubernetes**
    ```bash
    kubectl create deployment front-end-service --image=yourdockerhubusername/front-end-app:latest
    ```

4. **Exposer le service Kubernetes**
    ```bash
    kubectl expose deployment front-end-service --type=NodePort --port=8000
    minikube service front-end-service --url
    ```

5. **Configurer et appliquer les règles Ingress**
    ```bash
    kubectl apply -f ingress.yml
    kubectl get ingress
    minikube addons enable ingress-dns
    minikube tunnel
    ```

## Utilisation

1. Accédez à l'application via l'URL fournie par Minikube.
2. Ajoutez, modifiez et supprimez des tâches via l'interface utilisateur. (service 1)
3. Consultez les prévisions météorologiques pour n'importe quelle ville en utilisant le deuxième service. (de service 2 a service 1)

## Conclusion

Ce projet illustre la puissance et la flexibilité des technologies modernes pour le développement d'applications distribuées. En combinant Docker, Kubernetes, et une architecture de micro-services, nous avons pu créer une application scalable et maintenable, tout en approfondissant nos compétences en programmation distribuée.

 

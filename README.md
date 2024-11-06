# Odoo Security Project

This project demonstrates a security setup for an Odoo instance by deploying it in both unsecured and secured environments. In the unsecured environment, we simulate attacks to observe their effects, then repeat the tests with a secured configuration that includes protections against DDoS, brute-force, and SQL injection attacks.

## Prerequisites

- **Docker**: Make sure Docker is installed on your system.
- **Git**: Ensure Git is installed to clone the repository.

## Installation Guide

### Step 1: Install Docker

#### Install Docker from the Terminal
1. Open your terminal and run the following commands to install Docker:

    ```bash
    sudo apt update
    sudo apt install -y docker.io
    sudo systemctl start docker
    sudo systemctl enable docker
    ```

2. Verify Docker is installed:

    ```bash
    docker --version
    ```

#### Install Docker Desktop
Alternatively, you can [download Docker Desktop](https://www.docker.com/products/docker-desktop) for your operating system and follow the installation instructions provided on Docker's website.

### Step 2: Clone the Repository

In your terminal, navigate to the directory where you want to clone the project and run:

```bash
git clone https://github.com/yourusername/yourrepository.git
cd yourrepository
```

## Running the Unsecured Environment

1. **Start the Project with `no-secured-project.yml`:**

   Run the following command to start the Odoo instance in an unsecured environment:

   ```bash
   docker-compose -f no-secured-project.yml up -d --build
   ```

2. **Verify Odoo is Running:**

   Open your browser and navigate to [http://localhost:8069](http://localhost:8069). If Odoo loads successfully, the unsecured environment is up and running.

3. **Simulate Attacks:**

   To simulate attacks, enter each of the following commands in a separate terminal window.

   - **DDoS Attack:**

     ```bash
     docker exec -it attack_container_name sh
     python /scripts/ddos.py
     ```

   - **Brute Force Attack:**

     ```bash
     docker exec -it attack_container_name sh
     python /scripts/brute_force.py
     ```

   - **SQL Injection Attack:**

     ```bash
     docker exec -it attack_container_name sh
     python /scripts/sql_injection.py
     ```

4. **Observe the Effects:**

   Refresh [http://localhost:8069](http://localhost:8069) in your browser. The attacks should cause Odoo to become unresponsive or crash due to the lack of protection in this environment.

5. **Stop the Unsecured Environment:**

   After observing the effects, stop the unsecured environment:

   ```bash
   docker-compose -f no-secured-project.yml down -v
   ```

## Running the Secured Environment

1. **Start the Project with `secured-project.yml`:**

   Now, start the Odoo instance in the secured environment:

   ```bash
   docker-compose -f secured-project.yml up -d --build
   ```

2. **Verify Odoo is Running Securely:**

   Once again, navigate to [http://localhost:8069](http://localhost:8069) to confirm that Odoo is running.

3. **Simulate Attacks:**

   Repeat the same attacks as in the unsecured environment:

   - **DDoS Attack:**

     ```bash
     docker exec -it attack_container_name sh
     python /scripts/ddos.py
     ```

   - **Brute Force Attack:**

     ```bash
     docker exec -it attack_container_name sh
     python /scripts/brute_force.py
     ```

   - **SQL Injection Attack:**

     ```bash
     docker exec -it attack_container_name sh
     python /scripts/sql_injection.py
     ```

4. **Observe the Secured Environment’s Resilience:**

   Try refreshing [http://localhost:8069](http://localhost:8069) in your browser after each attack. The secured environment, equipped with protections, should remain responsive, or any malicious requests should be blocked, demonstrating the security configurations.

5. **Stop the Secured Environment:**

   After completing the tests, stop the secured environment:

   ```bash
   docker-compose -f secured-project.yml down -v
   ```

## Conclusion

This project demonstrates the impact of security configurations on an Odoo instance. The secured setup includes protections against common web attacks, providing a resilient environment for Odoo.

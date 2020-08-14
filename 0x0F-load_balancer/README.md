# 0x0F. Load balancer

For this project, look at these concepts:

* [Load balancer](https://en.wikipedia.org/wiki/Load_balancing_(computing))
* [Web stack debugging](https://www.google.com/search?q=what%20is%20web%20stack%20debugging)

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/275/qfdked8.png)

# Background Context
You have been given 2 additional servers:

* gc-[STUDENT_ID]-web-02-XXXXXXXXXX
* gc-[STUDENT_ID]-lb-01-XXXXXXXXXX

Lets improve our web stack so that there is [redundancy](https://en.wikipedia.org/wiki/Redundancy_%28engineering%29) for our web servers. This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.

For this project, you will need to write Bash scripts to automate your work. All scripts must be designed to configure a brand new Ubuntu server to match the task requirements.

# Resources
#### Read or watch:

* [Introduction to load-balancing and HAproxy](https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts)
* [HTTP header](https://www.techopedia.com/definition/27178/http-header)
* [Debian/Ubuntu HAProxy packages](https://haproxy.debian.net/)

# Tasks
#### [Tutorial](https://aws.amazon.com/es/premiumsupport/knowledge-center/linux-static-hostname/)
## 0. Double the number of webservers
## 1. Install your load balancer

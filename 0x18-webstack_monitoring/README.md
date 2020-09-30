# 0x18. Webstack monitoring

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/281/hb3pAsO.png)

## Background Context

You cannot fix or improve what you cannot measure is a famous saying in the Tech industry. In the age of the data-ism, monitoring how our Software systems are doing is an important thing. In this project, we will implement one of many tools to measure what is going on our servers.

Web stack monitoring can be broken down into 2 categories:
    * Application monitoring: getting data about your running software and making sure it is behaving as expected
    * Server monitoring: getting data about your virtual or physical server and making sure they are not overloaded (could be CPU, memory, disk or network overload)


## Resources
#### Read or watch:

* [What is server monitoring](https://www.sumologic.com/glossary/server-monitoring/)
* [What is application monitoring](https://en.wikipedia.org/wiki/Application_performance_management)
* [System monitoring by Google](https://landing.google.com/sre/sre-book/chapters/monitoring-distributed-systems/)
* [Nginx logging and monitoring](https://docs.nginx.com/nginx/admin-guide/monitoring/logging/)


## Learning Objectives

### General
* Why is monitoring needed
* What are the 2 main area of monitoring
* What are access logs for a web server (such as Nginx)
* What are error logs for a web server (such as Nginx)

# Tasks

## 0. Sign up for [Datadog](https://www.datadoghq.com/) and install datadog-agent
## 1. Monitor some metrics - [System check](https://docs.datadoghq.com/integrations/system/)
## 2. [Create a dashboard](./2-setup_datadog) - [Datadog's API](https://docs.datadoghq.com/api/v1/dashboards/#get-all-dashboards)

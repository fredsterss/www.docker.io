{% extends 'about.html' %}
{% block title %} About Docker {% endblock %}

{% block copy_1 %}

# DOCKER: AN INTRODUCTION

## ABOUT DOCKER

Docker  is an open-source engine that automates the deployment of any application as a lightweight, portable, self-sufficient container that will run virtually anywhere.

Docker containers can encapsulate any payload, and will run consistently on and between virtually any server. The same container that a developer builds and tests on a laptop will run at scale, in production, on VMs, bare-metal servers, OpenStack clusters, public instances, or combinations of the above.

Common use cases for Docker include:

*   Automating the packaging and deployment of applications
*   Creation of lightweight, private PAAS environments
*   Automated testing and continuous integration/deployment
*   Deploying and scaling web apps, databases and backend services

## BACKGROUND
	
Fifteen years ago, virtually all applications were written using well defined stacks of services and deployed on a single monolithic, proprietary server. Today, developers build and assemble applications using a multiplicity of the best available services, and must be prepared for those applications to be deployed across a multiplicity of different hardware environments, included public, private, and virtualized servers.

Figure 1: The Evolution of IT

This sets up the possibility for:

*   Adverse interactions between different services and "dependency hell"
*   Challenges in rapidly migrating and scaling across different hardware*   The impossibility of managing a matrix of multiple different services deployed across multiple different types of hardware

Figure 2: The Challenge of Multiple Stacks and Multiple Hardware Envrionments

Or, viewed as a matrix, we can see that there is a huge number of combinations and permutations of applications/services and hardware environments that need to be considered every time an application is written or rewritten. This creates a difficult situation for both the developers who are writing applications and the folks in operations who are trying to create a scalable, secure, and highly performance operations environment.

Figure 3: Dynamic Stacks and Dynamic Hardware Environments Create an NxN Matrix

How to solve this problem? A useful analogy can be drawn from the world of shipping. Before 1960, most cargo was shipped break bulk. Shippers and carriers alike needed to worry about bad interactions between different types of cargo (e.g. if a shipment of anvils fell on a sack of bananas). Similarly, transitions between different modes of transport were painful. Up to half the time to ship something could be taken up as ships were unloaded and reloaded in ports, and in waiting for the same shipment to get reloaded onto trains, trucks, etc. Along the way, losses due to damage and theft were large. And, there was an n X n matrix between a multiplicity of different goods and a multiplicity of different transport mechanisms.

Figure 4: Analogy: Shipping Pre-1960

Fortunately, an answer was found in the form of a standard shipping container.  Any type of goods, from pistachios to Porsches, can be packaged inside a standard shipping container. The container can then be sealed, and not re-opened until it reaches its final destination. In between, the containers can be loaded and unloaded, stacked, transported, and efficiently moved over long distances. The transfer from ship to gantry crane to train to truck can be automated, without requiring a modification of the container. Many authors credit the shipping container with revolutionizing both transportation and world trade in general. Today, 18 million standard containers carry 90% of world trade.

Figure 5: Solution to Shipping Challenge Was a Standard Container

To some extent, Docker can be thought of as an intermodal shipping container system for code. 

Figure 6: The Solution to Software Shipping is Also a Standard Container System

Docker enables any application and its dependencies to be packaged up as a lightweight, portable, self-sufficient container. Containers have standard operations, thus enabling automation. And, they are designed to run on virtually any Linux server. The same container that that a developer builds and tests on a laptop will run at scale, in production, on VMs, bare-metal servers, OpenStack clusters, public instances, or combinations of the above.

In other words, developers can build their application once, and then know that it can run consistently anywhere. Operators can configure their servers once, and then know that they can run any application.

## Why Should I Care (For Developers)

### Build once...run anywhere

"Docker interests me because it allows simple environment isolation and repeatability. I can create a run-time environment once, package it up, then run it again on any other machine. Furthermore, everything that runs in that environment is isolated from the underlying host (much like a virtual machine). And best of all, everything is fast and simple."

## Why Should I Care (For Devops)

### Configure once...run anything

*   Make the entire lifecycle more efficient, consistent, and repeatable
*   Increase the quality of code produced by developers
*   Eliminate inconsistencies between development, test, production, and customer environments
*   Support segregation of duties
*   Significantly improves the speed and reliability of continuous deployment and continuous integration systems
*   Because the containers are so lightweight, address significant performance, costs, deployment, and portability issues normally associated with VMs

## What are the Main Features of Docker

It is useful to compare the main features of Docker to those of shipping containers. (See the analogy above).

Figure 7: Main Docker Features

For a more technical view of features, please see the following:

*   Filesystem isolation: each process container runs in a completely separate root filesystem.
*   Resource isolation: system resources like cpu and memory can be allocated differently to each process container, using cgroups.
*   Network isolation: each process container runs in its own network namespace, with a virtual interface and IP address of its own.
*   Copy-on-write: root filesystems are created using copy-on-write, which makes deployment extremely fast, memory-cheap and disk-cheap.
*   Logging: the standard streams (stdout/stderr/stdin) of each process container is collected and logged for real-time or batch retrieval.
*   Change management: changes to a container's filesystem can be committed into a new image and re-used to create more containers. No templating or manual configuration required.
*   Interactive shell: docker can allocate a pseudo-tty and attach to the standard input of any container, for example to run a throwaway interactive shell.

## What are the Basic Docker Functions

Docker makes it easy to build, modify, publish, search, and run containers. The diagram below should give you a good sense of the Docker basics. With Docker, a container comprises both an application and all of its dependencies. Containers can either be created manually or, if a source code repository contains a DockerFile, automatically. Subsequent modifications to a baseline Docker image can be committed to a new container using the Docker Commit Function and then Pushed to a Central Registry.

Containers can be found in a Docker Registry (either public or private), using Docker Search. Containers can be pulled from the registry using Docker Pull and can be run, started, stopped, etc. using Docker Run commands. Notably, the target of a run command can be your own servers, public instances, or a combination. 

Figure 8: Basic Docker Functions

For a full list of functions, please go to: [http://docs.docker.io/en/latest/commandline/](http://docs.docker.io/en/latest/commandline/)

Docker runs three ways:
* as a daemon to manage LXC containers on your Linux host (sudo docker -d)
* as a CLI which talks to the daemon's REST API (docker run ...)
* as a client of Repositories that let you share what you've built (docker pull, docker commit).

## How Do Containers Work? (And How are they Different From VMs)

A container comprises an application and its dependencies. Containers serve to isolate processes which run in isolation in userspace on the host's operating system.

This differs significantly from traditional VMs. Traditional, hardware virtualization (e.g. VMWare, KVM, Xen, EC2) aims to create an entire virtual machine. Each virtualized application contains not only the application (which may only be 10's of MB) along with the binaries and libraries needed to run that application, and an entire Guest operating System (which may measure in 10s of GB).

The picture below captures the difference

Figure 9: Containers vs. Traditional VMs

Since all of the containers share the same operating system (and, where appropriate, binaries and libraries), they are significantly smaller than VMs, making it possible to store 100s of VMs on a physical host (versus a strictly limited number of VMs). In addition, since they utilize the host operating system, restarting a VM does not mean restarting or rebooting the operating system. Thus, containers are much more portable and much more efficient for many use cases.

With Docker Containers, the efficiencies are even greater. With a traditional VM, each application, each copy of an application, and each slight modification of an application requires creating an entirely new VM.

As shown above, a new application on a host need only have the application and its binaries/libraries. There is no need for a new guest operating system. 

If you want to run several copies of the same application on a host, you do not even need to copy the shared binaries.

Finally, if you make a modification of the application, you need only copy the differences.

Figure 10: Mechanism to Make Docker Containers Lightweight

This not only makes it efficient to store and run containers, it also makes it extremely easy to update applications. As shown in the next figure, updating a container only requires applying the differences.

Figure 11: Modfiying and Updating Containers

## What is the Relationship between Docker and dotCloud?

Docker is an open-source implementation of the deployment engine which powers dotCloud, a popular Platform-as-a-Service. It benefits directly from the experience accumulated over several years of large-scale operation and support of hundreds of thousands of applications and databases. dotCloud is the chief sponsor of the Docker project, and dotCloud CTO is the original architect and current, overall maintainer. While several dotCloud employees work on Docker full-time, Docker is a true community project, with hundreds of non-Docker contributors and a complete open design philosophy. All pulls, pushes, forks,  bugs, issues, and roadmaps are available for viewing, editing, and commenting on GitHub.

## What Are Some Cool Use Cases For Docker?

Docker is a powerful tool for many different use cases. Here are some great early use cases for Docker, as described by members of our community.

<table class="docker_use_cases_table">
	<thead>
		<tr>
			<td class="td1">
				Use Case
			</td>
			<td class="td2">
				Examples
			</td>
			<td class="td3">
				Link
			</td>
		</tr>
	</thead>
	<tbody>
		<tr class="tr_white">
			<td class="td1">
				Build your own PaaS
			</td>
			<td class="td2">
				Dokku - Docker powered mini-Heroku. The smallest PaaS implementation you’ve ever seen
			</td>
			<td class="td3">
				<a href="http://bit.ly/191Tgsx">http://bit.ly/191Tgsx</a>
			</td>
		</tr>
		<tr class="tr_blue">
			<td class="td1">
				Web Based Environment for Instruction
			</td>
			<td class="td2">
				JiffyLab – web based environment for the instruction, or lightweight use of, Python and UNIX shell
			</td>
			<td class="td3">
				<a href="http://bit.ly/12oaj2K">http://bit.ly/12oaj2K</a>
			</td>				
		</tr>
		<tr class="tr_white">
			<td class="td1" rowspan=3>
				Easy Application Deployment
			</td>
			<td class="td2">
				Deploy Java Apps With Docker = Awesome
			</td>
			<td class="td3">
				<a href="http://bit.ly/11BCvvux">http://bit.ly/11BCvvu</a>
			</td>
		</tr>
		<tr class="tr_white">
			<td class="td2">
				Running Drupal on Docker
			</td>
			<td class="td3">
				<a href="http://bit.ly/15MJS6B">http://bit.ly/15MJS6B</a>
			</td>
		</tr>	
		<tr class="tr_white">
			<td class="td2">
				Installing Redis on Docker
			</td>
			<td class="td3">
				<a href="http://bit.ly/16EWOKh">http://bit.ly/16EWOKh</a>
			</td>
		</tr>
		<tr class="tr_blue">
			<td class="td1">
				Create Secure Sandboxes
			</td>
			<td class="td2">
				Docker makes creating secure sandboxes easier than ever
			</td>
			<td class="td3">
				<a href="http://bit.ly/13mZGJH">http://bit.ly/13mZGJH</a>
			</td>				
		</tr>	
		<tr class="tr_white">
			<td class="td1">
				Create your own SaaS
			</td>
			<td class="td2">
				Memcached as a Service
			</td>
			<td class="td3">
				<a href="http://bit.ly/11nL8vh">http://bit.ly/11nL8vh</a>
			</td>				
		</tr>	
		<tr class="tr_blue">
			<td class="td1">
				Automated Application Deployment
			</td>
			<td class="td2">
				Push-button Deployment with Docker
			</td>
			<td class="td3">
				<a href="http://bit.ly/1bTKZTo">http://bit.ly/1bTKZTo</a>
			</td>				
		</tr>	
		<tr class="tr_white">
			<td class="td1">
				Continuous Integration and Deployment
			</td>
			<td class="td2">
				Next Generation Continuous Integration &amp; Deployment with dotCloud’s Docker and Strider
			</td>
			<td class="td3">
				<a href="http://bit.ly/ZwTfoy">http://bit.ly/ZwTfoy</a>
			</td>				
		</tr>
		<tr class="tr_blue">
			<td class="td1">
				Lightweight Desktop Virtualization
			</td>
			<td class="td2">
				Docker Desktop: Your Desktop Over SSH Running Inside Of A Docker Container
			</td>
			<td class="td3">
				<a href="http://bit.ly/14RYL6x">http://bit.ly/14RYL6x</a>
			</td>				
		</tr>					
	</tbody>
</table>

## How Can I get Started Using Docker

[Click here to get started](http://www.docker.io/gettingstarted/), including full instructions, code, and documentation. We've also prepared an interactive tutorial to help you get started.

## How Can I get a copy of the source code?

The Docker project is hosted on GitHub. [Click here to visit the repository](https://github.com/dotcloud/docker/).

## How Can I Join the Docker Community

Head on over to our [community] page

## How Can I Start Contributing to the Docker Project

We welcome contributions. Click here to learn more

{% endblock %}



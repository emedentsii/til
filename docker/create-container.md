1. Install Docker:

  `curl -fsSL https://get.docker.com/ | sh`

2. Then add your user to docker group. Something like that:

  `sudo usermod -aG docker genesys`

3. Build first Dockerfile. Docker support some command in docker files, here is few of them:
  - `FROM` - Point base container.
  - `ADD` - Add directories with needed files.
  - `RUN` - Execute command after container has built.
  - `CMD` - Execute after container start.

Download the .pem file.
Create a directory:
`# mkdir -p ~/.ssh`

Move the downloaded .pem file to the .ssh directory we just created:
`# mv ~/Downloads/ec2private.pem ~/.ssh`

Change the permissions of the .pem file so only the root user can read it:
`# chmod 400 ~/.ssh/ec2private.pem`

Create a config file:
`# vim ~/.ssh/config`

Enter the following text into that config file:
> Host *amazonaws.com
> IdentityFile ~/.ssh/ec2private.pem
> User ec2-user

Save that file.
Use the ssh command with your public DNS hostname to connect to your instance.
e.g.:
`# ssh ec2-54-23-23-23-34.example.amazonaws.com`
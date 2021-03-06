# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > `head <filename>` displays first ten lines of filename 
> > `cd` navigate to parent directory i.e. `cd desktop`
> > `cat <filename>` open the contents of filename 
> > `whois <domain>` output whois information for domain 
> > `curl` used to download files from a url - like the pull we did in the application
> > `clear` clear the command line window 
> > `touch <filename>` update file access and mod time 
> > `top` output information on processes that are currently running 
> > `kill <process ID>` quit processes with process ID 
> > `find <dir> -name "<filename>` find files named filename in directory named dir 



---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

`ls`  list directory contents 
`ls -a`  list files in directory 
`ls -l`  long format instead of bare format
`ls -lh`  long format, human readable 
`ls -lah`  long format, human readable, all files 
`ls -t`  files listed in order of last modified 
`ls -Glp`  no group, long format, with file type

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > `ls -i`
> > `ls -o`
> > `ls -u`
> > `ls -r`
> > `ls -c`

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > Creates command lines from standard input and executes them. xargs can be used to take the output from one command and use it as the argument for a separate command. xargs can break up a command that exceeds maximum size. 

 


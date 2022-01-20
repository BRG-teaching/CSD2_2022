# [NVM](https://github.com/nvm-sh/nvm)
`nvm` allows you to quickly install and use different versions of node via the command line.

## Install NVM
Run the command bash script in the terminal. <br/>
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
```
Verrify the installation
```bash
command -v nvm
```

## Useful Commands
`nvm ls`: list locally installed version
`nvm ls-remote`: lists all available versions
`nvm install 10.21.0` install the correct node version for Gitbook
`nvm use 10.21.0`: switch to and use the installed 10.21.0 version
`g`: the path to the installed node version
`nvm --help`: help documents

## Alternative: NodeJs
Download [Node.js](https://nodejs.org/en/). Note that the node version should be **`10.21.0`**. 

`node -v`: check node version
`npm -v`: check npm version

## Gitbook Installation
```
npm install gitbook-cli -g
```
install gitbook (`V` is capital!):
```
gitbook -V
``` 
or 
```
gitbook init
```

This error might happen, which is normally casue by the version compatibility. 
```bash
TypeError: cb.apply is not a function
```
Go to the npm directory. For Mac:
```bash
cd /opt/local/lib/node_modules/gitbook-cli/node_modules/npm/node_modules
```
Windows:
```bash
C:\Users\duch\AppData\Roaming\npm\node_modules\gitbook-cli\node_modules\npm\node_modules>
````
Run the following command.
```bash
npm install graceful-fs@latest --save
```
## Run Gitbook
Initiate the gitbook. It create `README.md` and `SUMMARY.md` in the current directory they don't exist. 
```bash
gitbook init
```
Build Gitbook
```bash
gitbook build
```
After editting, recompile the gitbook. This command will create the folder named `_book` if it doens't exist yet. The folder contains the static web pages that we can not only host through github pages, but also any other hosting service online. 
```bash
gitbook serve
```
After startup, open this URL in the browser: `http://localhost:4000`


[User Manual (Chinese)](https://chrisniael.gitbooks.io/gitbook-documentation/content/index.html)

## Import files
If import files to the gitbook, remember to edit the `SUMMARY.md` file to link to other markdown files. The summary should look like this: 
```
# Summary

* [Chapter 1](chapter1.md)
* [Chapter 2](chapter2.md)
* [Chapter 3](chapter3.md)
```

## Synchronize static site code to branch
Synchronize the built static website code to `gh-pages` In the branch.

Run `publish.sh` script to automate creation of gh-pages

## Output PDF
Output the Pdf requires installation of `gitbook pdf`
But.. this can also be easily done on Gitbook.io
```
npm install gitbook-pdf -g
```




<!-- 
### [Method 2](https://www.npmjs.com/package/@gitbook-ng/gitbook): 
If the first method doesn't work, try the second method. (It works for me..)
If you have tried the first method, first you need to uninstall `gitbook-cli`.
```bash
npm uninstall gitbook-cli -g
rm -fr ~/.gitbook   # Remove legacy gitbook global installation 
```
Now get start. 
```bash
npm install @gitbook-ng/gitbook
```

If there's no `package.json` under the folder, you can run: `npm init -y ` to create one. 

Add `build` and `serve` commands to `package.json`:
```json
"scripts": {
  "serve": "gitbook serve",
  "build": "gitbook build",
}
```
Run:
```bash
npx gitbook init
```
```bash
npm run build
```
```bash
npm run serve
``` -->


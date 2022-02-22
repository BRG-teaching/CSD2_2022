# RV2

![](../.gitbook/assets/plugin\_title\_slides\_compas\_rv2.jpg)

The Rhinoceros® plug-in RhinoVAULT, developed by Dr. Matthias Rippmann at the Block Research Group at ETH Zurich, emerged from research on structural form finding using the Thrust Network Analysis (TNA) approach to intuitively create and explore compression-only structures.

Using reciprocal diagrams, RhinoVAULT provides an intuitive, fast funicular form-finding method, adopting the same advantages of techniques such as Graphic Statics, but offering a viable extension to three-dimensional problems. Our goal is to share a transparent setup to let you not only create beautiful shapes but also to give you an understanding of the underlying structural principles.

RhinoVAULT 2 (RV2) is an open-source research and development platform for funicular form-finding built with [COMPAS](https://compas-dev.github.io), a Python-based framework for computational research and collaboration in Architecture, Engineering, and Digital Fabrication.

RV2 is a Rhino plugin that replaces RhinoVAULT for Rhino versions 6 and above. Unlike RhinoVAULT, RV2 no longer relies on Rhino for its computational implementation. Instead, it is built entirely with open source packages from the COMPAS ecosystem and will, therefore, be available not only for Rhino and Grasshopper, but also for Blender and other tools with a Python scripting interface, and ultimately even in the browser.

For more information about RV2, please visit the [RV2 documentation](https://blockresearchgroup.gitbook.io/rv2/).

## 0. Preparation <a href="#0.-preparation" id="0.-preparation"></a>

Open Rhino and run the command `EditPythonScript` once, then exit Rhino (this will initialize some internal Rhino folder structure which is necessary for the installation of RV2).​

![](https://gblobscdn.gitbook.com/assets%2F-M8u9kpnS1-yoLoBjTSo%2F-MAwE-2oelyRRa35UBgK%2F-MAwHk3YzPESfNQGXEUd%2F0.PNG?alt=media\&token=66886fe0-e7ca-45c1-8294-f5fcd2823b69)

## 1. Download <a href="#1.-download" id="1.-download"></a>

Download latest RV2 (v1.1.4) installation file from [https://github.com/BlockResearchGroup/compas-RV2/releases/tag/v1.1.4](https://github.com/BlockResearchGroup/compas-RV2/releases/tag/v1.1.4).​

![](https://gblobscdn.gitbook.com/assets%2F-M8u9kpnS1-yoLoBjTSo%2F-MAqXaUGYQ7uQPkq0HM-%2F-MAqYVsT1BTxeCjQEF8R%2F1.PNG?alt=media\&token=8d8082b8-caa6-4e21-98a2-83ef460311b4)

## 2. Install <a href="#2.-install" id="2.-install"></a>

Run the installation file. If you see following prompt, click on `More info` then choose `Run anyway`&#x20;

![](https://gblobscdn.gitbook.com/assets%2F-M8u9kpnS1-yoLoBjTSo%2F-MAqXaUGYQ7uQPkq0HM-%2F-MAqYeVWYc1Y4fK\_YUiW%2F3a.PNG?alt=media\&token=8ed02ad7-cb52-4bc7-bfa8-5ec9d0eb60d9)

After the installation interface shows up, click on the **`Install RV2`** button, then choose a location to install RV2 on your computer.

After the installation interface shows up, click on the **`Install RV2`** button, then choose a location to install RV2 on your computer.

{% hint style="warning" %}
RV2 is a Rhino plugin. It is not software. We just need an installation location to set up some of the dependencies for the plugin.&#x20;

Therefore, you can choose any folder for the installation, as long as there are no spaces in the installation path!\
\
Paths like`D:\Program Files\...`will fail to install.\
\
However, please, **don't use your "Program Files" folder for the installation** process since this requires special admin privileges. Instead, use something like:\
\
`C:/Tools`\
`C:/RhinoVault2`\
`C:/DF2020`\
`C:/Users/username/Documents`\
`C:/Users/username/Desktop`
{% endhint %}

![](https://gblobscdn.gitbook.com/assets%2F-M8u9kpnS1-yoLoBjTSo%2F-MAqXaUGYQ7uQPkq0HM-%2F-MAqYn7MiC1KLDnP\_GIu%2F4a.png?alt=media\&token=93f1e11f-cf92-40b1-8392-e93f1810f99c)



The installation usually takes 1\~2 minutes. After the progress bar finishes, click **`Yes`** twice in User Account Control.

![](https://gblobscdn.gitbook.com/assets%2F-M8u9kpnS1-yoLoBjTSo%2F-MAqXaUGYQ7uQPkq0HM-%2F-MAqYuQ1U5EVau45BN5k%2Finstall\_finish.png?alt=media\&token=53a82ebe-3e96-4faf-b5c0-cfaa12518638)

The installation is successful if you see this message:

![](../.gitbook/assets/image.png)

{% hint style="info" %}
Note that you have to close the installer window after the installation.&#x20;
{% endhint %}

## 3. Activate Toolbar in Rhino

In the top menu, go to `Tools > Toolbar Layout`.

![](https://gblobscdn.gitbook.com/assets%2F-M5MfAgazp\_fa5cV9Mju%2F-M5aEI69gsiLrzdWpPWJ%2F-M5aQXm0DhXh3UhiWAHe%2Finstallation-05.png?alt=media\&token=b888d3d9-81a4-4113-a8e7-7120fea7143f)

In the pop-up window, click `File > Open`.&#x20;

![](https://gblobscdn.gitbook.com/assets%2F-M5MfAgazp\_fa5cV9Mju%2F-M5aEI69gsiLrzdWpPWJ%2F-M5aQaDeOjyszk-Y1QgG%2Finstallation-06.png?alt=media\&token=d231a5ea-7801-4dbf-9fdf-0c5a6cf58d2c)

Go to the location where your RV2 is installed, for example `D:\MySoftwares\RV2\` , enter the folder called `dev` then find the file `RV2.rui` and open it.

![](https://gblobscdn.gitbook.com/assets%2F-M8u9kpnS1-yoLoBjTSo%2F-MAqXaUGYQ7uQPkq0HM-%2F-MAqZD7zoR45mRS2lQ47%2Frui.PNG?alt=media\&token=476aaf75-fe78-442f-9364-44475543fae8)

Tick `RV2` in the Toolbars section.

![](https://gblobscdn.gitbook.com/assets%2F-M8u9kpnS1-yoLoBjTSo%2F-MAz\_7-yz1vBeWVqgunJ%2F-MAza7PygmGyMtGwIjRN%2Ftoobar.PNG?alt=media\&token=7ff9292b-715e-4716-97c0-d9fedc078e41)

The RV2 menu and toolbar will now both appear in user interface.

![](https://gblobscdn.gitbook.com/assets%2F-M8u9kpnS1-yoLoBjTSo%2F-MAqXaUGYQ7uQPkq0HM-%2F-MAqZLMsEOHFtyhdBXJI%2Fmenu.PNG?alt=media\&token=9fefe8b8-57f7-43c9-bb08-ed110787f34e)

## 4. Initialise RV2

To check that everything worked, click the `Initialise RV2` menu item or toolbar button. You will be asked to accept the "Terms and Conditions" and "User Agreement" (just click `Yes` :) after which the welcome screen should disappear.

![](https://gblobscdn.gitbook.com/assets%2F-M8u9kpnS1-yoLoBjTSo%2F-MAzSIgXSwNoNaGLTUqz%2F-MAzSZ21kOOC9F35-QZE%2Fintialise.PNG?alt=media\&token=a8b5e52d-b69c-4326-8761-e4746b829d23)

If the initialization step fails, please file an issue on the [RV2 issue tracker](https://github.com/BlockResearchGroup/compas-RV2/issues/) and we will help you as quickly as possible.

If Rhino says `Command not found: -_RV2init`, please type `EditPythonScript` to open the script editor and restart Rhino. Then try the initialisation again.


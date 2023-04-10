# Sat-Hacking-卫星安全由入门到精通
 该GitHub仓库是一个卫星安全的学习资源库，收集了卫星安全的入门和高级资料，包括学习教程、工具和参考资料等。可以帮助安全爱好者快速入门和掌握卫星安全领域的知识和技能。其中包括卫星通信、控制系统、指挥和控制、天线和信号处理等方面的内容，适合对卫星安全领域感兴趣的人士学习和探索。
 同时，这个仓库也欢迎卫星安全领域的专家和爱好者参与贡献，共同建设这个资源库，推动卫星安全领域的发展。

![Image text](./group/sat-banner.png)   
<p align="center">Sat-Hacking官方LOGO</p>



 ## Sat-Hacking- 博客系列学习路线
卫星安全是当前信息安全领域的一个热点话题，为了帮助安全从业者更好地了解卫星安全领域的相关概念和技术，我们推出了卫星安全博客系列。该系列博客将从基本的卫星通信协议和工作原理入手，介绍卫星通信的各个方面，包括卫星通信的物理层、数据链路层、网络层和应用层等，同时探讨卫星通信中存在的安全问题和攻击方式，并提供相应的防御措施。

卫星安全博客系列将分为多个篇章，每个篇章将围绕特定的主题展开，内容丰富、系统性强，适合各个层次的读者。我们将介绍卫星通信中的常见协议和标准，如GPS、Glonass、Beidou、Galileo等，同时深入研究卫星信号的特点和调制方式，以及卫星通信中的安全机制和攻击手段。此外，我们还将介绍如何使用各种工具和技术来分析和保护卫星通信系统的安全性，包括使用软件定义无线电（SDR）和GNURadio等工具进行卫星信号分析、使用漏洞扫描工具检测卫星通信系统中的漏洞、以及使用加密算法和认证技术来保护卫星通信系统的机密性和完整性。

我们希望通过卫星安全博客系列，为安全从业者提供一条清晰的学习路线，帮助他们深入了解卫星通信和卫星安全领域的相关技术和知识，提高他们的技能水平，并为卫星安全领域的发展做出贡献。卫星安全博客系列将持续更新，为读者提供更多的学习资源和实战演练，敬请关注。

## Sat-Hacking安全系列博客学习路线


### [Sat-Hacking：Starlink卫星通信频段](https://blog.csdn.net/weixin_68076304/article/details/129583780?csdn_share_tail=%7B%22type%22%3A%22blog%22%2C%22rType%22%3A%22article%22%2C%22rId%22%3A%22129583780%22%2C%22source%22%3A%22weixin_68076304%22%7D) 

了解卫星通信频段是学习卫星安全的基础理论知识，卫星通信频段是指用于卫星通信的无线电波频谱范围。在卫星通信中，无线电波在地面站与卫星之间传输信息，实现通信和数据传输。为了使各种卫星和地面系统之间的通信有效且互不干扰，国际电信联盟（ITU）将频谱划分为不同的频段，分配给不同的卫星通信服务。

更多学习资料可加入本文末尾社区QQ群获取。

![Image text](./group/satinspace.png)   
<p align="center">科技卫星</p>


### [Sat-Hacking：hackasat无线通信类CTF深度剖析](https://blog.csdn.net/weixin_68076304/article/details/129451741?spm=1001.2014.3001.5501) 

当准备参加Hack-A-Sat CTF比赛时，最好的方法是从过去的Hack-A-Sat活动中练习挑战，特别是与Comms Systems/RF相关的挑战。这些挑战通常涉及与无线通信和射频技术相关的问题和任务，需要熟悉相关概念和技术。

练习使用无线通信相关工具和技术，例如SDR（软件定义无线电）和GNURadio，来模拟和分析无线信号和通信系统，了解射频和无线通信基础知识，并练习使用相关工具和技术，是准备参加Hack-A-Sat CTF比赛中与Comms Systems/RF相关的挑战的最佳方法。

博客中所用到的演示代码可从StarLink_UE目录下或加入本文末尾社区QQ群获取。

![Image text](./group/sat-1.png)   
<p align="center">卫星安全黑客</p>



### [Sat-Hacking：Starlink终端逆向分析](https://blog.csdn.net/weixin_68076304/article/details/129526961?spm=1001.2014.3001.5502) 

Starlink终端是SpaceX推出的卫星互联网终端设备，它的目的是为了提供高速、低延迟的卫星互联网服务。该终端设备采用了一种平板天线设计，可以自动搜索、跟踪并连接卫星信号，同时还具有数据处理、无线网络传输等多种功能。在 Starlink 卫星互联网系统中，用户设备端采用了专门设计的 UE 终端，可以实现与卫星网络的连接和通信。为了更好地了解 Starlink UE 终端的工作原理和内部结构，我们对其进行了固件进行了逆向分析。

本文将分享 Starlink UE 终端的硬件和软件架构，Starlink固件的逆向方法以及其相关的通信协议和安全机制。希望通过这篇文章，为大家提供有关 Starlink UE 终端的详细信息和技术参考，以促进更广泛的技术交流和研究。

博客中所用到的演示代码可从StarLink_UE目录下或加入本文末尾社区QQ群获取。

![Image text](./group/satstation.jpg)   
<p align="center">卫星地面接收站</p>


### [Sat-Hacking：路由器逆向分析-上篇](https://blog.csdn.net/weixin_68076304/article/details/129776236?csdn_share_tail=%7B%22type%22%3A%22blog%22%2C%22rType%22%3A%22article%22%2C%22rId%22%3A%22129776236%22%2C%22source%22%3A%22weixin_68076304%22%7D) 

在本篇文章中，我们将探讨 SpaceX Starlink 路由器的逆向分析过程。Starlink 是 SpaceX 推出的一项革命性的卫星互联网服务，旨在为全球偏远地区提供高速、低延迟的互联网连接。为了实现这一目标，Starlink 需要一个高性能的路由器来管理用户的互联网连接。逆向分析这种设备对于理解其工作原理和潜在的安全隐患至关重要。    

博客中所用到的演示代码可从StarLink_router目录下或加入本文末尾社区QQ群获取。

![Image text](./group/starlinkrouter.png)   
<p align="center">starlink路由器</p>


### [Sat-Hacking：路由器逆向分析-中篇](https://blog.csdn.net/weixin_68076304/article/details/129843763?csdn_share_tail=%7B%22type%22%3A%22blog%22%2C%22rType%22%3A%22article%22%2C%22rId%22%3A%22129843763%22%2C%22source%22%3A%22weixin_68076304%22%7D) 

随着技术的不断发展和创新，SpaceX 已经推出了第二代 Starlink 路由器，这一代路由器拥有更高的性能和更多的功能，为用户提供更好的卫星互联网服务体验。在本文中，我们将对 SpaceX Starlink 路由器二代进行深入探讨，了解它的功能和工作原理，以及可能的逆向分析方法。

博客中所用到的演示代码可从starlink-wifi-gen2目录下或加入本文末尾社区QQ群获取。

![Image text](./group/starlink-dish-and-router.jpg)   
<p align="center">starlink路由器</p>


### [Sat-Hacking（6）：Starlink路由器逆向分析-下篇](https://blog.csdn.net/weixin_68076304/article/details/129893882?spm=1001.2014.3001.5502) 

在之前文章中，我们介绍了 SpaceX Starlink 路由器二代的工作原理和逆向分析过程，以及该路由器在提供卫星互联网服务方面的重要性。接下来继续分析SpaceX Starlink 路由器二代的开源代码。

博客中所用到的演示代码可从StarLink_router目录下或加入本文末尾社区QQ群获取。

![Image text](./group/starlinkrouter.png)   
<p align="center">starlink路由器</p>


### [Sat-Hacking基础篇：iptables路由流量到云主机代理（上）](https://mp.weixin.qq.com/s?__biz=Mzg3MzkzMDUzMg==&mid=2247483710&idx=1&sn=bf08935fa7d910f0c416b76af4bc1d81&chksm=ced9cb75f9ae426309725a1afba110aed10c35e056250e83aff6bbd054a17d9787b8276a875a&token=494562786&lang=zh_CN#rd) 

最近在做路由器安全审计，为starlink的路由审计继续做准备工作。

假设我们已经获得了路由器的root权限，接下来要通过云主机上安装和配置Tinyproxy代理服务器，并将路由器上的流量透明地转发到代理服务器上，然后实现HTTP和HTTPS劫持来修改用户请求的目标网站。

卫星网络安全方面，代理服务器同样可以用于加密和保护用户的流量，以确保敏感数据在通过卫星网络传输时不被窃取或篡改。此外，在某些情况下，代理服务器也可以用于控制和监视网络流量，以便进行安全审计和调查。故将本文作为卫星网络安全的基础文章来介绍。

更多代码可以加入本文末尾社区QQ群获取。

![Image text](./group/router.jpg)   
<p align="center"></p>




### [Sat-Hacking基础篇：QEMU 模拟MIPS架构环境](https://blog.csdn.net/weixin_68076304/article/details/129601382?csdn_share_tail=%7B%22type%22%3A%22blog%22%2C%22rType%22%3A%22article%22%2C%22rId%22%3A%22129601382%22%2C%22source%22%3A%22weixin_68076304%22%7D) 

在本篇文章中，我们将探讨如何使用 QEMU 模拟器模拟 MIPS架构设备的启动过程。MIPS 是一种具有硬件级安全性和实时性能的处理器架构，尤其适用于卫星系统等对安全性和实时性有严格要求的领域。

本文将详细介绍如何利用 QEMU 模拟器在 MIPS 架构设备上进行卫星系统的安全性研究。QEMU 是一款开源的、跨平台的虚拟化软件，它支持多种处理器架构，能够提供硬件级别的仿真，使得开发人员能够在不同平台上进行软件调试和验证。


文中所用到的启动文件请从mipsel文件夹下获取，读者也加入本文末尾社区QQ群获取更多卫星网络安全学习资料。

![Image text](./group/chip.png)   
<p align="center">mips芯片概念图</p>





## 加入Sat-Hacking社区
* 若初学者面临环境搭建问题以及自身搭建环境出现困难的情况下，也可以加入QQ群获取测试环境镜像，可以直接在虚拟机里面运行测试代码，镜像包含Vmware安装程序及Windows环境下的所有测试程序。
* 加入QQ群需要您捐赠20元人民币，申请入群时贴上转账单号即可，您的捐赠将鼓励我继续完善Web渗透安全博客的系列。
* 单笔超过500元的捐赠者，您将可以参与Sat-Hacking的编辑，一同梳理Sat-Hacking博客系列。
![Image text](./group/joingroup.png)
如果以上的图裂了，可以下载图片（支付宝 | 微信）到本地进行扫描。


## 感谢

在我的安全从业过程中，我非常感激那些给予我指导和帮助的老师和同学。现在，我希望把我学习的内容传递给其他人，帮助他们进入Sat-Hacking安全领域，成为一名有价值的安全从业者。

我非常珍视这些宝贵的经验和知识，并希望能够将这些内容分享给其他人。我相信，通过我的分享和传递，更多的人将加入Sat-Hacking安全领域，并为卫星安全事业做出自己的贡献。

## 免责声明

Sat-Hacking系列的任何内容均无意教导或鼓励将安全工具或方法用于非法或不道德的网络入侵行为。

使用任何安全工具或技术时，读者应该始终保持负责任的态度，并遵守相关的法律和道德规范。我们建议读者在使用此处描述的任何工具或技术之前，先获得相关人员的书面许可，并将其应用于合法和道德的网络安全研究和测试活动中。
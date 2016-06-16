1. [install oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh)  
>sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"

2. 微调一些配置  
修改~/.zshrc
 * 喜欢的主题  
 ZSH_THEME="ys"
 * 禁用自动进入目录，防止命令歧义 
 unsetopt AUTO_CD
3. 登陆默认使用zsh  
sudo chsh -s /bin/zsh ubuntu

# GIVE ME YOUR FRIES! 更新日志

2026 年 11 月 12 日 · 当前版本 **v2.2** · [GitHub 游戏文件](https://github.com/sd5913/Fun-interactive-game-with-two-person-cameras/blob/main/GIVE_ME_YOUR_FRIES_DUO_GESTURE.html)

## v2.2 · 游客塔防

- **抓到第一根薯条就会触发警戒。** 附近的游客头顶亮起叹号，地图上出现固定的红圈，游戏播放预警音并显示倒计时。
- 三关的撤离时间依次为 **1.65 秒、1.50 秒和 1.35 秒**。归零时游客发动范围攻击，红圈内的海鸥会被短暂击晕，脚上抓到的薯条全部掉落。
- 及时飞出红圈可以保住脚上的薯条。已带回巢穴的分数保留。

[查看 v2.2 提交](https://github.com/sd5913/Fun-interactive-game-with-two-person-cameras/commit/775d33ca64f872be677d5d5e6f95b18cc9b293b0)

## v2.1 · 双人手势与摄像头

- 把摄像头框移到两个计分栏之间、地图上缘，两个巢穴都能看见。
- 手势识别、摄像头预览和手部描线使用同一帧镜像画面，修正描线错位。
- 加快海鸥对手掌移动的响应，并按画面比例校正捏合距离。手短暂越过摄像头中线时，仍控制原来的海鸥。

[查看 v2.1 提交](https://github.com/sd5913/Fun-interactive-game-with-two-person-cameras/commit/956b97d5eeddcfe9f943d76bc027ef3094169d09)

## v2 · 模式、头像与偷薯条

- 新增单人和双人模式。单人使用整个镜头，双人各用镜头的一侧，在同一张大地图上飞行，各有自己的巢穴。
- 开局可以拍头像、上传照片或用默认头像。P1 是金帽海鸥，P2 是蓝巾海鸥，羽色也做了区分。
- 张手飞行，捏合抓薯条。抓到的薯条会直接画在海鸥脚上，飞行时也看得见。
- 移除用手势偷走整盒薯条的功能。鼠标或触屏可以重新摆放薯条盒，盒子落到海面或跨出岸边时会回到原位。
- 修复手离开镜头后海鸥自动回巢的问题。手出镜时海鸥停在原地并保留抓到的薯条，在镜头内主动松开手指仍可回巢。

[查看 v2 提交](https://github.com/sd5913/Fun-interactive-game-with-two-person-cameras/commit/56209d47ee86fcd9624770fc7b1b25d99218e893) · [查看初版备份](https://github.com/sd5913/Fun-interactive-game-with-two-person-cameras/tree/backup/pre-v2-2026-11-12)

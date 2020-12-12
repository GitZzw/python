# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt  # 用来绘制图形
plt.figure(figsize=(20, 10))
plt.ion()
for point_i in range(1, n_plot_points):
    # for agent_i in range(2):
    #     print('Dyna ' + str(agent_i) + ', Episode ' + str((point_i+1)*eps_per_point))
    #     agents[agent_i].train(eps_per_point)
    #     benchmark_data[agent_i][point_i] = agents[agent_i].benchmark(eps_benchmark)

    print('DynaQ' + ', Episode ' + str((point_i+1)*eps_per_point))
    agents[0].train(eps_per_point)
    benchmark_data[0][point_i] = agents[0].benchmark(eps_benchmark)
    print('Dyna2' + ', Episode ' + str((point_i+1)*eps_per_point))
    agents[1].train(eps_per_point)
    benchmark_data[1][point_i] = agents[1].benchmark(eps_benchmark)


# Plot results
# plt.figure(figsize=(16, 10))
# xaxis = [eps_per_point*(i+1) for i in range(n_plot_points)]
# title1 = 'DynaQ'
# title4 = 'Dyna2'
# titles = [title1, title4]
# for i in range(2):
#     plt.subplot(221+i)
#     plt.plot(xaxis, benchmark_data[i])
#     plt.xlabel('Training episodes')
#     plt.ylabel('Average reward per episode')
#     plt.title(titles[i])
# plt.show()
    # Plot results
    plt.clf()  # 清除之前画的图
    fig = plt.gcf()  # 获取当前图
    xaxis = [eps_per_point*(i+1) for i in range(n_plot_points)]
    title1 = 'DynaQ'
    title4 = 'Dyna2'
    titles = [title1, title4]
    for i in range(2):
        plt.subplot(121+i)
        plt.plot(xaxis, benchmark_data[i])
        plt.xlabel('Training episodes')
        plt.ylabel('Average reward per episode')
        plt.title(titles[i])
    plt.pause(0.001)  # 暂停一段时间，不然画的太快会卡住显示不出来
    plt.ioff()  # 关闭画图窗口Z
plt.show()
compareMethods()

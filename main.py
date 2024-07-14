from medical_data_visualizer import draw_cat_plot, draw_heat_map

# Generate and save the cat plot
fig_cat = draw_cat_plot()
fig_cat.savefig('catplot.png')

# Generate and save the heat map
fig_heat = draw_heat_map()
fig_heat.savefig('heatmap.png')

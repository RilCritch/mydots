--[[
#=====================================================================================
#                               ArcoLinuxD
#
# Author  : Erik Dubois at http://www.erikdubois.be
# License : Distributed under the terms of GNU GPL version 2 or later
# Documentation : http://erikdubois.be/category/linux/aureola/
#======================================================================================


]]


conky.config = {

	--Various settings
	background = true, 							    -- forked to background
	cpu_avg_samples = 2,						    -- The number of samples to average for CPU monitoring.
	diskio_avg_samples = 10,		  	    -- The number of samples to average for disk I/O monitoring.
	double_buffer = true,						    -- Use the Xdbe extension? (eliminates flicker)
	if_up_strictness = 'address',		    -- how strict if testing interface is up - up, link or address
	net_avg_samples = 2,						    -- The number of samples to average for net data
	no_buffers = true,							    -- Subtract (file system) buffers from used memory?
	temperature_unit = 'fahrenheiht',		-- fahrenheit or celsius
	text_buffer_size = 2048,	  		    -- size of buffer for display of content of large variables - default 256
	update_interval = 1,						    -- update interval
	imlib_cache_size = 0,               -- disable image cache to get a new spotify cover per song


	--Placement
	alignment = 'top_right',    -- top-left,top-middle,top-right,bottom-left,bottom-middle,bottom-right,
                              -- middle-left,middle-middle,middle-right,none
	--Arch Duoscreen
	--gap_x = -1910,
	gap_x = 16,   		        -- pixels between right or left border
	gap_y = 76,						    -- pixels between bottom or left border
	minimum_height = 1320,    -- minimum height of window
	minimum_width = 260,			-- minimum height of window
	maximum_width = 260,		  -- maximum height of window

	--Graphical
	border_inner_margin = 9,0, 					    -- margin between border and text
	border_outer_margin = 0, 					    -- margin between border and edge of window
	border_width = 0, 							      -- border width in pixels
	-- default_bar_width = 29,					    -- default is 0 - full width
	default_bar_height = 6,					    -- default is 6
	default_gauge_height = 25,					  -- default is 25
	default_gauge_width = 40,					    -- default is 40
	default_graph_height = 40,					  -- default is 25
	-- default_graph_width = 153,					  -- default is 0 - full width
	default_shade_color = '#0c0e0f',			-- default shading colour
	default_outline_color = '#78b892',    -- default outline colour
	draw_borders = false,						      -- draw borders around text
	draw_graph_borders = true,					  -- draw borders around graphs
	draw_shades = false,						      -- draw shades
	draw_outline = false,						      -- draw outline
	stippled_borders = 0,						      -- dashing the border

	--Textual

	extra_newline = false,						-- extra newline at the end - for asesome's wiboxes
	format_human_readable = true,				-- KiB, MiB rather then number of bytes
	-- font = 'Noto Mono:size=11:regular',  			-- font for complete conky unless in code defined
	-- font = 'JetBrainsMono Nerd Font Mono:size=12',  			-- font for complete conky unless in code defined
	font = 'Ubuntu:pixelsize=16',  			-- font for complete conky unless in code defined
	max_text_width = 0,							-- 0 will make sure line does not get broken if width too smal
	max_user_text = 16384,						-- max text in conky default 16384
	override_utf8_locale = true,				-- force UTF8 requires xft
	short_units = true,							-- shorten units from KiB to k
	top_name_width = 21,						-- width for $top name value default 15
	top_name_verbose = false,					-- If true, top name shows the full command line of  each  process - Default value is false.
	uppercase = false,							-- uppercase or not
	use_spacer = 'none',						-- adds spaces around certain objects to align - default none
	use_xft = true,								-- xft font - anti-aliased font
	xftalpha = 1,								-- alpha of the xft font - between 0-1

	--Windows
	own_window = true,							                                                -- create your own window to draw
	own_window_argb_value = 190,			                                              -- real transparency - composite manager required 0-255
	own_window_argb_visual = true,				                                          -- use ARGB - composite manager required
	own_window_class = 'Conky',					                                            -- manually set the WM_CLASS name for use with xprop
	own_window_colour = '#0c0e0f',				                                          -- set colour if own_window_transparent no
	own_window_hints = 'undecorated,below,above,sticky,skip_taskbar,skip_pager',    -- if own_window true - just hints - own_window_type sets it
	own_window_transparent = false,				                                          -- if own_window_argb_visual is true sets background opacity 0%
	own_window_title = 'system_conky',			                                        -- set the name manually  - default conky "hostname"
	own_window_type = 'dock',				                                                -- if own_window true options are: normal/override/dock/desktop/panel


	--Colours

	default_color = '#edeff0',  				-- default color and border color
	color1 = '#edeff0',
	color2 = '#7d7f80',
	color3 = '#505253',
	color4 = '#343637',
	color5 = '#1f2112',
	color6 = '#6791c9',
	color7 = '#78b892',  						--green
	color8 = '#ecd28b',  						--orange
	color9 = '#df5b61',  						--firebrick


	--Lua
  template7 = [[${voffset -3}${color3}${top name \1}${alignr}${top cpu \1}%]],
  template8 = [[${voffset -3}${color3}${top_mem name \1}${alignr}${top_mem mem_res \1}]],


};
conky.text = [[
${voffset -15}
${color7}${alignr}${font Ubuntu:style=Medium:pixelsize=55}${time %I:%M}${font}
${voffset -10}
${color6}${alignr}${time %A}${font}
${color2}${voffset 3}${alignr}${time %B %d, %Y}
#${color7}${hr}


${color7}${font Mononoki Nerd Font :size=20} ${offset 6}${voffset 2}${font Ubuntu:style=Medium:pixelsize=22}System  ${color2}${voffset 3}${hr}${font}
${font Ubuntu:pixelsize=15}${voffset -10}
${color6}${nodename} ${color2}(${machine})${alignr}${color2}$kernel${color}
${voffset -15}
${color2}Uptime:${color2}${alignr}${uptime}${color}
${voffset -15}
${color2}Processes:${color2}${alignr}${running_processes}/${processes}${color}


${color7}${font Mononoki Nerd Font :size=20} ${offset 6}${voffset 2}${font Ubuntu:style=Medium:pixelsize=22}CPU  ${color2}${voffset 3}${hr}${font}
${font Ubuntu:pixelsize=15}${voffset -10}
${color6}AMD Ryzen 9 6900HX${alignr}${if_match ${cpu cpu0}<50}${color2}\
${else}${if_match ${cpu cpu0}>=50}${color8}\
${else}${if_match ${cpu cpu0}>=90}${color9}${endif}${cpu cpu0}%${color}
${voffset -15}
${if_match ${cpu cpu0}<100}${color2}\
${else}${if_match ${cpu cpu0 }==100}${color9}${endif}\
${cpugraph cpu0 -l}${color}${font}
#
${voffset -3}${color6}process${alignr}${color2}cpu
${font Ubuntu:pixelsize=14}${voffset 2}${template7 1}
${template7 2}
${template7 3}
${template7 4}
${template7 5}
${template7 6}
${template7 7}


${color7}${font Mononoki Nerd Font :size=20} ${offset 6}${voffset 2}${font Ubuntu:style=Medium:pixelsize=22}Memory  ${color2}${voffset 3}${hr}${font}
${font Ubuntu:pixelsize=15}${voffset -10}
${color6}Used${alignr}${color2}${mem}/${memmax}
#
${voffset -15}
${color2}${voffset 1}${membar}
#
${color2}Swap${color3}${offset 10}${voffset 1}${swapbar}
#
${voffset -10}
${color6}process${alignr}${color2}mem
${font Ubuntu:pixelsize=14}${voffset 3}${template8 1}
${template8 2}
${template8 3}
${template8 4}
${template8 5}
${template8 6}
${template8 7}


${color7}${font Mononoki Nerd Font :size=20}󰋊 ${offset 6}${offset -8}${voffset 2}${font Ubuntu:style=Medium:pixelsize=22}Storage  ${color2}${voffset 3}${hr}${font}
${font Ubuntu:pixelsize=15}${voffset -10}
${color6}Root ${color2}(${fs_type})${alignr}${color2}${fs_used /}/${fs_size /}
${color2}${voffset 1}${fs_bar /}


${color7}${font Mononoki Nerd Font :size=20} ${offset 6}${voffset 2}${font Ubuntu:style=Medium:pixelsize=22}Keybindings  ${color2}${voffset 3}${hr}${font}
${font Ubuntu:pixelsize=15}${voffset -10}
${color2}[S] + [Shift] + r${alignr}${color6}Application Menu
${voffset -10}
${color2}[S] + [Shift]+ q${alignr}${color6}Kill Focused App
${voffset -10}
${color2}[S] + [Shift] + b${alignr}${color6}Open Browser
${voffset -10}
${color2}[S] + enter${alignr}${color6}Open Terminal
#
${color4}${hr 1}
${voffset 2}${color2}[S] + [Shift] + s${alignr}${color6}System Options
${voffset -10}
${color2}[S] + [Shift] + c${alignr}${color6}Clipboard View
${voffset -10}
${color2}[S] + [Ctrl] + x${alignr}${color6}Power Menu
#
${color4}${hr 1}
${voffset 2}${color2}[S] + [Shift] + f${alignr}${color6}Scratch Terminal
${voffset -10}
${color2}[S] + b${alignr}${color6}All Keybindings


${color7}${voffset 5}${font Ubuntu:style=Medium:pixelsize=45}Qtile${alignr -5}${color6}${voffset -25}${font}${font Mononoki Nerd Font:size=60} ${font}
${voffset -35}
${color3}${offset 4}${font Ubuntu:pixelsize=14}${voffset 6}Configured in Python
${voffset -50}
]];


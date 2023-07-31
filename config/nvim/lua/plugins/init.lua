#!/usr/bin/env lua


return {
	{
  	  	-- LSP Configuration & Plugins
		'neovim/nvim-lspconfig',
  	  	dependencies = {
		    -- Automatically install LSPs to stdpath for neovim
		    { 'williamboman/mason.nvim', config = true },
  	        'williamboman/mason-lspconfig.nvim',

  	        -- Useful status updates for LSP
  	        -- NOTE: `opts = {}` is the same as calling `require('fidget').setup({})`
  	    	{ 'j-hui/fidget.nvim', tag = 'legacy', opts = {} },

  	   		-- Additional lua configuration, makes nvim stuff amazing!
  	   		'folke/neodev.nvim',
  	  	},
  	},

  	{
		-- Autocompletion
  	  	'hrsh7th/nvim-cmp',
  	  	dependencies = {
  			-- Snippet Engine & its associated nvim-cmp source
  	  	  	'L3MON4D3/LuaSnip',
  	  	  	'saadparwaiz1/cmp_luasnip',

  	  	  	-- Adds LSP completion capabilities
  	  	  	'hrsh7th/cmp-nvim-lsp',

  	  	  	-- Adds a number of user-friendly snippets
  	  	  	'rafamadriz/friendly-snippets',
  	  	},
  	},

  	{  	-- Useful plugin to show you pending keybinds.
		'folke/which-key.nvim',
		opts = {},
	},

  	{
  		-- Adds git releated signs to the gutter, as well as utilities for managing changes
		'lewis6991/gitsigns.nvim',
  	  	opts = function()
  			return require 'plugins.configs.gitsigns'
  	  	end,
  	},

	{
		'norcalli/nvim.lua',
	},

	{
		'norcalli/nvim-base16.lua',
	},

  	{
  		-- Add indentation guides even on blank lines
  	  	'lukas-reineke/indent-blankline.nvim',
  	  	-- Enable `lukas-reineke/indent-blankline.nvim`
  	  	-- See `:help indent_blankline.txt`
  	  	opts = {
			-- char_blankline = '󰘍',
  	  	  	show_trailing_blankline_indent = false,
			context_char_bankline = "",
			show_current_context = true,
			show_current_context_start_on_current_line = false,
  	  	},
  	},

  	{  	-- "gc" to comment visual regions/lines
		'numToStr/Comment.nvim',
		opts = {}
	},

  	{ 	-- Fuzzy Finder (files, lsp, etc)
		'nvim-telescope/telescope.nvim',
		branch = '0.1.x',
		dependencies = {
			'nvim-lua/plenary.nvim',
		}
	},

  	{
  		'nvim-telescope/telescope-fzf-native.nvim',
  	  	-- NOTE: If you are having trouble with this installation,
  	  	--       refer to the README for telescope-fzf-native for more instructions.
  	  	build = 'make',
  	  	cond = function()
  	  		return vim.fn.executable 'make' == 1
  	  	end,
  	},

  	{
  		-- Highlight, edit, and navigate code
  	  	'nvim-treesitter/nvim-treesitter',
  	  	dependencies = {
  	  		'nvim-treesitter/nvim-treesitter-textobjects',
  	  	},
  	  	build = ':TSUpdate',
  	},


	{ -- statusline on the bottom
		'nvim-lualine/lualine.nvim',
  		dependencies = { 'nvim-tree/nvim-web-devicons' },
		opts = function()
		    return require "plugins.configs.lualine"
		end,
	},

	{ -- buffer file manager and navigator
		'stevearc/oil.nvim',
  		opts = function()
			return require "plugins.configs.oil"
		end,
  		dependencies = { "nvim-tree/nvim-web-devicons" },
	},

	{ -- changes color of current line number to match mode colors
		'mawkler/modicator.nvim',
  		-- init = function()
  		--   	-- These are required for Modicator to work
  		--   	vim.o.cursorline = true
  		-- end,
  		config = function()
  		  	require('modicator').setup()
  		end,
	},

    {
        'akinsho/bufferline.nvim',
        version = "*",
        dependencies = 'nvim-tree/nvim-web-devicons',
        config = function()
            require("bufferline").setup {
                options = { -- need to figure finish adding everything for configuration
                    mode = "buffers", -- or "tabs"
                    -- style_preset = require("bufferline").style_preset.no_italic,
                    themable = true, -- or false
                    numbers = "none", -- or "ordinal" | "buffer_id" | "both" | function({ ordinal, id, lower, raise}): string
                    close_command = "bdelete! %d",
                    right_mouse_command = "bdelete! %d",
                    left_mouse_command = "buffer %d",
                    middle_mouse_command = nil,
                    indicator = {
                        -- icon = '▎',
                        icon = '▊',
                        style = 'icon', -- or 'icon' | 'underline' | 'none
                    },
                    buffer_close_icon = '󰅖',
                    modified_icon = '●',
                    close_icon = '',
                    left_trunc_marker = '',
                    right_trunc_marker = '',
                    -- name_formatter = function(buf) -- buf contains: name, path, bufnr(buffer only), buffers and tabnr(tabs only)
                    --     buf.
                    -- end,
                    max_name_length = 18,
                    max_prefix_length = 15,
                    truncate_names = true,
                    tab_size = 18,
                    diagnostics = false, -- or "nvim_lsp" | "coc"
                    diagnostics_update_in_insert = false,
                    diagnostics_indicator = function(count, level, diagnostic_dict, context)
                        return "("..count..")"
                    end,
                    -- custom_filter = function(buf_number, buf_numbers)
                    --      -- filter out filetypes you don't want to see
                    --     if vim.bo[buf_number].filetype ~= "<i-dont-want-to-see-this>" then
                    --         return true
                    --     end
                    --     -- filter out by buffer name
                    --     if vim.fn.bufname(buf_number) ~= "<buffer-name-I-dont-want>" then
                    --         return true
                    --     end
                    --     -- filter out based on arbitrary rules
                    --     -- e.g. filter out vim wiki buffer from tabline in your work repo
                    --     if vim.fn.getcwd() == "<work-repo>" and vim.bo[buf_number].filetype ~= "wiki" then
                    --         return true
                    --     end
                    --     -- filter out by it's index number in list (don't show first buffer)
                    --     if buf_numbers[1] ~= buf_number then
                    --         return true
                    --     end
                    -- end,
                    offsets = {
                        {
                            -- filetype = "NvimTree",
                            -- text = "File Explorer", -- or function
                            text_align = "center", -- or "left" | "right"
                            separator = true,
                        }
                    },
                    color_icons = false, -- or true
                    show_buffer_icons = false, -- or false
                    show_buffer_close_icons = true, -- or false
                    show_close_icon = true, -- or false
                    show_tab_indicators = true, -- or false
                    show_duplicate_prefix = true, -- or false
                    persist_buffer_sort = true, -- or false
                    move_wraps_at_ends = false,
                    -- separator_style = "slope", -- or "slant" | "slope" | "thick" | "thin" | { 'any', 'any' },
                    -- separator_style = {'', ''}, -- or "slant" | "slope" | "thick" | "thin" | { 'any', 'any' },
                    enforce_regular_tabs = false, -- or true
                    always_show_bufferline = true, -- or false
                    hover = {
                        enabled = true, -- or false
                        delay = 200,
                        reveal = {'close'},
                    },
                    sort_by = 'insert_at_end', -- or 'insert_after_current' | 'id' | 'extension' 'relative_directory' | 'directory' | 'tabs' | function
                },
            }
        end,
    },
}

-- vim: ts=4 sts=4 sw=4 et

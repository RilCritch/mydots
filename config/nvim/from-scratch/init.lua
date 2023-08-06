#!/usr/bin/env lua
-- vim:fileencoding=utf-8:foldmethod=marker

-- Description: Where every part of nvim config is brought togehter
--
--
-- Author: RilCritch
--
--
-- Date Created: July 25, 2023

-- Set <space> as the leader key
-- See `:help mapleader`
--  NOTE: Must happen before plugins are required (otherwise wrong leader will be used)
vim.g.mapleader = " "
vim.g.maplocalleader = " "

----------------------------------------------------------- vim options {{{
-- See `:help vim.o`

-- Set highlight on search
vim.o.hlsearch = false

-- Make line numbers default
vim.wo.number = true
vim.wo.relativenumber = true

-- Enable mouse mode
vim.o.mouse = "a"
vim.o.mousemoveevent = true

-- Sync clipboard between OS and Neovim.
--  Remove this option if you want your OS clipboard to remain independent.
--  See `:help 'clipboard'`
vim.o.clipboard = "unnamedplus"

-- Enable break indent
vim.o.breakindent = true

-- Save undo history
vim.o.undofile = true

-- Case-insensitive searching UNLESS \C or capital in search
vim.o.ignorecase = true
vim.o.smartcase = true

-- Keep signcolumn on by default
vim.wo.signcolumn = "yes"

-- Decrease update time
vim.o.updatetime = 250
vim.o.timeoutlen = 300

-- Set completeopt to have a better completion experience
vim.o.completeopt = "menuone,noselect"

-- folds
vim.o.foldmethod = "marker"

-- NOTE: You should make sure your terminal supports this
vim.o.termguicolors = true

-- look and feel
vim.o.cursorline = true
vim.o.cursorcolumn = true
vim.o.cmdheight = 0

-- tabs
vim.o.tabstop = 4
vim.o.softtabstop = 4
vim.o.shiftwidth = 4
-- }}}

----------------------------------------------------------- package manager - lazy {{{
local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not vim.loop.fs_stat(lazypath) then
	vim.fn.system({
		"git",
		"clone",
		"--filter=blob:none",
		"https://github.com/folke/lazy.nvim.git",
		"--branch=stable", -- latest stable release
		lazypath,
	})
end
vim.opt.rtp:prepend(lazypath)

-- load plugins from plugins directory
require("lazy").setup("plugins")
-- }}}

----------------------------------------------------------- themimg {{{
-- Theme
local theme = {
	bg = "#0c0e0f",
	lightbg = "#1f2122",
	lighterbg = "#27292a",
	fg = "#acb5b9",
	black = "#141617",
	white = "#edeff0",
	red = "#df5b61",
	orange = "#e89982",
	green = "#78b892",
	blue = "#6791c9",
	yellow = "#ecd28b",
	gray = "#505253",
	darkgray = "#343637",
	lightgray = "#7d7f80",
}

local base16 = require("themes.base16")
base16(base16.themes.yoru, true)

-- setting hightlights look up :help nvim_set_hl for detailed info
-- EX: vim.api.nvim_set_hl({namespace_id}0=global, '{hl_group_name}', {vals})
-- general highlights
vim.api.nvim_set_hl(0, "CursorLine", { bg = theme.lightbg })
vim.api.nvim_set_hl(0, "CursorLineNr", { fg = theme.lightgray })

-- hightlights for modicator
vim.api.nvim_set_hl(0, "NormalMode", { fg = theme.lightgray })
vim.api.nvim_set_hl(0, "InsertMode", { fg = theme.blue })
vim.api.nvim_set_hl(0, "VisualMode", { fg = theme.green })
vim.api.nvim_set_hl(0, "CommandMode", { fg = theme.yellow })
vim.api.nvim_set_hl(0, "ReplaceMode", { fg = theme.orange })
vim.api.nvim_set_hl(0, "SelectMode", { fg = theme.lightgray })
vim.api.nvim_set_hl(0, "TerminalMode", { fg = theme.lightgray })
vim.api.nvim_set_hl(0, "TerminalNormalMode", { fg = theme.lightgray })

-- highlights for bufferline
vim.api.nvim_set_hl(0, "BufferLineDevIconDefaultSelected", { fg = theme.blue, bg = theme.lighterbg })
vim.api.nvim_set_hl(0, "BufferLineDevIconDefaultInactive", { fg = theme.lightgray })
vim.api.nvim_set_hl(0, "BufferLineCloseButtonSelected", { fg = theme.fg, bg = theme.lighterbg })
vim.api.nvim_set_hl(0, "BufferLineCloseButtonVisible", { fg = theme.lightgray })
vim.api.nvim_set_hl(0, "BufferLineCloseButton", { fg = theme.lightgray })
vim.api.nvim_set_hl(0, "BufferLineTab", { fg = theme.lightgray, bold = true })
vim.api.nvim_set_hl(0, "BufferLineTabSelected", { fg = theme.green, bold = true })
vim.api.nvim_set_hl(0, "BufferLineTabSeparatorSelected", { fg = theme.fg })
vim.api.nvim_set_hl(0, "BufferLineTabSeparator", { fg = theme.fg })
vim.api.nvim_set_hl(0, "BufferLineTabClose", { fg = theme.lightgray })
vim.api.nvim_set_hl(0, "BufferLineSeparator", { fg = theme.gray })
vim.api.nvim_set_hl(0, "BufferLineSeparatorSelected", { fg = theme.gray })
vim.api.nvim_set_hl(0, "BufferLineSeparatorVisible", { fg = theme.gray })
vim.api.nvim_set_hl(0, "BufferLineGroupSeparator", { fg = theme.fg })
vim.api.nvim_set_hl(0, "BufferLineGroupLabel", { fg = theme.bg, bg = theme.lightgray, bold = true })
vim.api.nvim_set_hl(0, "BufferLineOffsetSeparator", { fg = theme.lightgray })
vim.api.nvim_set_hl(0, "BufferLineIndicatorSelected", { fg = theme.green, bg = theme.lighterbg, bold = true })
vim.api.nvim_set_hl(0, "BufferLineIndicatorVisible", { fg = theme.lightgray })
vim.api.nvim_set_hl(0, "BufferLineDuplicate", { fg = theme.blue, italic = true })
vim.api.nvim_set_hl(
	0,
	"BufferLineDuplicateSelected",
	{ fg = theme.blue, bg = theme.lighterbg, italic = true, bold = true }
)
vim.api.nvim_set_hl(0, "BufferLineDuplicateActive", { fg = theme.blue, italic = true })
vim.api.nvim_set_hl(0, "BufferLineDuplicateVisible", { fg = theme.blue, italic = true })
vim.api.nvim_set_hl(0, "BufferLineModified", { fg = theme.orange })
vim.api.nvim_set_hl(0, "BufferLineModifiedSelected", { fg = theme.orange, bg = theme.lighterbg })
vim.api.nvim_set_hl(0, "BufferLineModifiedVisible", { fg = theme.orange })
vim.api.nvim_set_hl(0, "BufferLineNumbers", { fg = theme.lightgray })
vim.api.nvim_set_hl(0, "BufferLineNumbersSelected", { fg = theme.green, bg = theme.lighterbg, bold = true })
vim.api.nvim_set_hl(0, "BufferLineNumbersVisible", { fg = theme.lightgray })
vim.api.nvim_set_hl(0, "BufferLineBuffer", { fg = theme.lightgray })
vim.api.nvim_set_hl(0, "BufferLineBufferSelected", { fg = theme.fg, bg = theme.lighterbg, bold = true })
vim.api.nvim_set_hl(0, "BufferLineBufferVisible", { fg = theme.lightgray })
vim.api.nvim_set_hl(0, "BufferLinePick", { fg = theme.red, bold = true })
vim.api.nvim_set_hl(0, "BufferLinePickSelected", { fg = theme.red, bg = theme.lighterbg, bold = true })
vim.api.nvim_set_hl(0, "BufferLinePickVisible", { fg = theme.red, bold = true })
vim.api.nvim_set_hl(0, "BufferLineInfo", { fg = theme.lightgray })
vim.api.nvim_set_hl(0, "BufferLineInfoSelected", { fg = theme.fg, bg = theme.lighterbg, bold = true })
vim.api.nvim_set_hl(0, "BufferLineInfoVisible", { fg = theme.lightgray })
vim.api.nvim_set_hl(0, "BufferLineHint", { fg = theme.lightgray })
vim.api.nvim_set_hl(0, "BufferLineHintSelected", { fg = theme.fg, bg = theme.lighterbg, bold = true })
vim.api.nvim_set_hl(0, "BufferLineHintVisible", { fg = theme.lightgray })
vim.api.nvim_set_hl(0, "BufferLineTruncMarker", { fg = theme.lightgray })
vim.api.nvim_set_hl(0, "BufferLineBackground", { fg = theme.fg })
vim.api.nvim_set_hl(0, "BufferLineFill", { fg = theme.lightgray })

-- look and feel shit vim opts
vim.o.list = true
vim.opt.listchars:append("tab:  ")
vim.opt.listchars:append("trail:█")
-- }}}

----------------------------------------------------------- plugin config needed in main {{{
-- highlights for indent_blankline
vim.cmd([[highlight IndentBlanklineIndent1 guifg=#27292a gui=nocombine]])
vim.cmd([[highlight IndentBlanklineIndent2 guifg=#27292a gui=nocombine]])
vim.cmd([[highlight IndentBlanklineIndent3 guifg=#27292a gui=nocombine]])
vim.cmd([[highlight IndentBlanklineIndent4 guifg=#27292a gui=nocombine]])
vim.cmd([[highlight IndentBlanklineIndent5 guifg=#27292a gui=nocombine]])
vim.cmd([[highlight IndentBlanklineIndent6 guifg=#27292a gui=nocombine]])
vim.cmd([[highlight IndentBlanklineIndent7 guifg=#27292a gui=nocombine]])
vim.cmd([[highlight IndentBlanklineIndent8 guifg=#27292a gui=nocombine]])
vim.cmd([[highlight IndentBlanklineIndent9 guifg=#27292a gui=nocombine]])
vim.cmd([[highlight IndentBlanklineContextChar guifg=#78b892 gui=nocombine]])
vim.cmd([[highlight IndentBlanklineSpaceChar guifg=#27292a gui=nocombine]])
-- indent_blankline options
require("indent_blankline").setup({
	space_char_blankline = " ",
	char_highlight_list = {
		"IndentBlanklineIndent1",
		"IndentBlanklineIndent2",
		"IndentBlanklineIndent3",
		"IndentBlanklineIndent4",
		"IndentBlanklineIndent5",
		"IndentBlanklineIndent6",
		"IndentBlanklineIndent7",
		"IndentBlanklineIndent8",
		"IndentBlanklineIndent9",
	},
})

-- }}}

----------------------------------------------------------- basic keymaps {{{

-- Keymaps for better default experience
-- See `:help vim.keymap.set()`
vim.keymap.set({ "n", "v" }, "<Space>", "<Nop>", { silent = true })

-- Remap for dealing with word wrap
vim.keymap.set("n", "k", "v:count == 0 ? 'gk' : 'k'", { expr = true, silent = true })
vim.keymap.set("n", "j", "v:count == 0 ? 'gj' : 'j'", { expr = true, silent = true })

-- easier command mode activation
vim.keymap.set("n", ";", ":", { desc = "Easy command mode" })
-- }}}

----------------------------------------------------------- auto commands {{{
-- [[ Highlight on yank ]]
-- See `:help vim.highlight.on_yank()`
local highlight_group = vim.api.nvim_create_augroup("YankHighlight", { clear = true })
vim.api.nvim_create_autocmd("TextYankPost", {
	callback = function()
		vim.highlight.on_yank()
	end,
	group = highlight_group,
	pattern = "*",
})
-- }}}

----------------------------------------------------------- telescope config {{{
-- See `:help telescope` and `:help telescope.setup()`
require("telescope").setup({
	defaults = {
		mappings = {
			i = {
				["<C-u>"] = false,
				["<C-d>"] = false,
			},
		},
	},
})

-- Enable telescope fzf native, if installed
pcall(require("telescope").load_extension, "fzf")

-- See `:help telescope.builtin`
vim.keymap.set("n", "<leader>?", require("telescope.builtin").oldfiles, { desc = "[?] Find recently opened files" })
vim.keymap.set("n", "<leader><space>", require("telescope.builtin").buffers, { desc = "[ ] Find existing buffers" })
vim.keymap.set("n", "<leader>/", function()
	-- You can pass additional configuration to telescope to change theme, layout, etc.
	require("telescope.builtin").current_buffer_fuzzy_find(require("telescope.themes").get_dropdown({
		winblend = 10,
		previewer = false,
	}))
end, { desc = "[/] Fuzzily search in current buffer" })

vim.keymap.set("n", "<leader>gf", require("telescope.builtin").git_files, { desc = "Search [G]it [F]iles" })
vim.keymap.set("n", "<leader>sf", require("telescope.builtin").find_files, { desc = "[S]earch [F]iles" })
vim.keymap.set("n", "<leader>sh", require("telescope.builtin").help_tags, { desc = "[S]earch [H]elp" })
vim.keymap.set("n", "<leader>sw", require("telescope.builtin").grep_string, { desc = "[S]earch current [W]ord" })
vim.keymap.set("n", "<leader>sg", require("telescope.builtin").live_grep, { desc = "[S]earch by [G]rep" })
vim.keymap.set("n", "<leader>sd", require("telescope.builtin").diagnostics, { desc = "[S]earch [D]iagnostics" })
-- }}}

----------------------------------------------------------- treesitter config {{{
-- See `:help nvim-treesitter`
require("nvim-treesitter.configs").setup({
	-- Add languages to be installed here that you want installed for treesitter
	ensure_installed = { "c", "cpp", "go", "lua", "python", "rust", "tsx", "typescript", "vimdoc", "vim" },

	-- Autoinstall languages that are not installed. Defaults to false (but you can change for yourself!)
	auto_install = false,

	highlight = { enable = true },
	indent = { enable = true },
	incremental_selection = {
		enable = true,
		keymaps = {
			init_selection = "<c-space>",
			node_incremental = "<c-space>",
			scope_incremental = "<c-s>",
			node_decremental = "<M-space>",
		},
	},
	textobjects = {
		select = {
			enable = true,
			lookahead = true, -- Automatically jump forward to textobj, similar to targets.vim
			keymaps = {
				-- You can use the capture groups defined in textobjects.scm
				["aa"] = "@parameter.outer",
				["ia"] = "@parameter.inner",
				["af"] = "@function.outer",
				["if"] = "@function.inner",
				["ac"] = "@class.outer",
				["ic"] = "@class.inner",
			},
		},
		move = {
			enable = true,
			set_jumps = true, -- whether to set jumps in the jumplist
			goto_next_start = {
				["]m"] = "@function.outer",
				["]]"] = "@class.outer",
			},
			goto_next_end = {
				["]M"] = "@function.outer",
				["]["] = "@class.outer",
			},
			goto_previous_start = {
				["[m"] = "@function.outer",
				["[["] = "@class.outer",
			},
			goto_previous_end = {
				["[M"] = "@function.outer",
				["[]"] = "@class.outer",
			},
		},
		swap = {
			enable = true,
			swap_next = {
				["<leader>a"] = "@parameter.inner",
			},
			swap_previous = {
				["<leader>A"] = "@parameter.inner",
			},
		},
	},
})
-- }}}

----------------------------------------------------------- diagnostic keymaps {{{
vim.keymap.set("n", "[d", vim.diagnostic.goto_prev, { desc = "Go to previous diagnostic message" })
vim.keymap.set("n", "]d", vim.diagnostic.goto_next, { desc = "Go to next diagnostic message" })
vim.keymap.set("n", "<leader>e", vim.diagnostic.open_float, { desc = "Open floating diagnostic message" })
vim.keymap.set("n", "<leader>q", vim.diagnostic.setloclist, { desc = "Open diagnostics list" })
vim.keymap.set("n", "<leader>dh", vim.diagnostic.hide, { desc = "Hide Diagnostics" })
vim.keymap.set("n", "<leader>ds", vim.diagnostic.show, { desc = "Show Diagnostics" })
vim.keymap.set("n", "<leader>dd", vim.diagnostic.disable, { desc = "Disable Diagnostics" })
vim.keymap.set("n", "<leader>de", vim.diagnostic.enable, { desc = "Enable Diagnostics" })
-- }}}

----------------------------------------------------------- lsp configuration {{{
--  This function gets run when an LSP connects to a particular buffer.
local on_attach = function(_, bufnr)
	-- NOTE: Remember that lua is a real programming language, and as such it is possible
	-- to define small helper and utility functions so you don't have to repeat yourself
	-- many times.
	--
	-- In this case, we create a function that lets us more easily define mappings specific
	-- for LSP related items. It sets the mode, buffer and description for us each time.
	local nmap = function(keys, func, desc)
		if desc then
			desc = "LSP: " .. desc
		end

		vim.keymap.set("n", keys, func, { buffer = bufnr, desc = desc })
	end

	nmap("<leader>rn", vim.lsp.buf.rename, "[R]e[n]ame")
	nmap("<leader>ca", vim.lsp.buf.code_action, "[C]ode [A]ction")

	nmap("gd", vim.lsp.buf.definition, "[G]oto [D]efinition")
	nmap("gr", require("telescope.builtin").lsp_references, "[G]oto [R]eferences")
	nmap("gI", vim.lsp.buf.implementation, "[G]oto [I]mplementation")
	nmap("<leader>D", vim.lsp.buf.type_definition, "Type [D]efinition")
	nmap("<leader>dt", require("telescope.builtin").lsp_document_symbols, "[D]ocument [S]ymbols")
	nmap("<leader>ws", require("telescope.builtin").lsp_dynamic_workspace_symbols, "[W]orkspace [S]ymbols")

	-- See `:help K` for why this keymap
	nmap("K", vim.lsp.buf.hover, "Hover Documentation")
	nmap("<C-k>", vim.lsp.buf.signature_help, "Signature Documentation")

	-- Lesser used LSP functionality
	nmap("gD", vim.lsp.buf.declaration, "[G]oto [D]eclaration")
	nmap("<leader>wa", vim.lsp.buf.add_workspace_folder, "[W]orkspace [A]dd Folder")
	nmap("<leader>wr", vim.lsp.buf.remove_workspace_folder, "[W]orkspace [R]emove Folder")
	nmap("<leader>wl", function()
		print(vim.inspect(vim.lsp.buf.list_workspace_folders()))
	end, "[W]orkspace [L]ist Folders")

	-- Create a command `:Format` local to the LSP buffer
	vim.api.nvim_buf_create_user_command(bufnr, "Format", function(_)
		vim.lsp.buf.format()
	end, { desc = "Format current buffer with LSP" })
end

-- Enable the following language servers
--  Feel free to add/remove any LSPs that you want here. They will automatically be installed.
--
--  Add any additional override configuration in the following tables. They will be passed to
--  the `settings` field of the server config. You must look up that documentation yourself.
--
--  If you want to override the default filetypes that your language server will attach to you can
--  define the property 'filetypes' to the map in question.
local servers = {
	-- clangd = {},
	-- gopls = {},
	-- pyright = {},
	-- rust_analyzer = {},
	-- tsserver = {},
	-- html = { filetypes = { 'html', 'twig', 'hbs'} },

	lua_ls = {
		Lua = {
			workspace = { checkThirdParty = false },
			telemetry = { enable = false },
		},
	},
}

-- Setup neovim lua configuration
require("neodev").setup()

-- nvim-cmp supports additional completion capabilities, so broadcast that to servers
local capabilities = vim.lsp.protocol.make_client_capabilities()
capabilities = require("cmp_nvim_lsp").default_capabilities(capabilities)

-- Ensure the servers above are installed
local mason_lspconfig = require("mason-lspconfig")

mason_lspconfig.setup({
	ensure_installed = vim.tbl_keys(servers),
})

mason_lspconfig.setup_handlers({
	function(server_name)
		require("lspconfig")[server_name].setup({
			capabilities = capabilities,
			on_attach = on_attach,
			settings = servers[server_name],
			filetypes = servers[server_name].filetypes,
		})
	end,
})
-- }}}

----------------------------------------------------------- nvim-cmp configuration {{{
-- See `:help cmp`
local cmp = require("cmp")
local luasnip = require("luasnip")
require("luasnip.loaders.from_vscode").lazy_load()
luasnip.config.setup({})

cmp.setup({
	snippet = {
		expand = function(args)
			luasnip.lsp_expand(args.body)
		end,
	},
	mapping = cmp.mapping.preset.insert({
		["<C-n>"] = cmp.mapping.select_next_item(),
		["<C-p>"] = cmp.mapping.select_prev_item(),
		["<C-d>"] = cmp.mapping.scroll_docs(-4),
		["<C-f>"] = cmp.mapping.scroll_docs(4),
		["<C-Space>"] = cmp.mapping.complete({}),
		["<CR>"] = cmp.mapping.confirm({
			behavior = cmp.ConfirmBehavior.Replace,
			select = true,
		}),
		["<Tab>"] = cmp.mapping(function(fallback)
			if cmp.visible() then
				cmp.select_next_item()
			elseif luasnip.expand_or_locally_jumpable() then
				luasnip.expand_or_jump()
			else
				fallback()
			end
		end, { "i", "s" }),
		["<S-Tab>"] = cmp.mapping(function(fallback)
			if cmp.visible() then
				cmp.select_prev_item()
			elseif luasnip.locally_jumpable(-1) then
				luasnip.jump(-1)
			else
				fallback()
			end
		end, { "i", "s" }),
	}),

	sources = {
		{ name = "nvim_lsp" },
		{ name = "luasnip" },
	},
})
-- }}}

----------------------------------------------------------- testing {{{
require("plugins.configs.luasnip")
-- }}}

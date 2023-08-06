-- vim:fileencoding=utf-8:foldmethod=marker

-- Keymaps are automatically loaded on the VeryLazy event
-- Default keymaps that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/keymaps.lua
-- Add any additional keymaps here

-- This file is automatically loaded by lazyvim.config.init

-- This code at the top was found at the link above
-- local Util = require("lazyvim.util")

local function map(mode, lhs, rhs, opts)
  local keys = require("lazy.core.handler").handlers.keys
  ---@cast keys LazyKeysHandler
  -- do not create the keymap if a lazy keys handler exists
  if not keys.active[keys.parse({ lhs, mode = mode }).id] then
    opts = opts or {}
    opts.silent = opts.silent ~= false
    if opts.remap and not vim.g.vscode then
      opts.remap = nil
    end
    vim.keymap.set(mode, lhs, rhs, opts)
  end
end

-- LazyVim overrides {{{
--
-- }}}

-- utility
map("n", ";", ":", { desc = "Quick command mode" })

-- colorizer
map("n", "<leader>cc", "<cmd>ColorizerToggle<cr>", { desc = "Toggle color highlighting" })
map("n", "<leader>ce", "<cmd>ColorizerAttachToBuffer<cr>", { desc = "Enable color highlighting" })

-- windows
map("n", "<leader>wo", "<C-W>o", { desc = "Close all other windows", remap = true })

-- markdown
map("n", "<leader>mc", "<cmd>MdEval<cr>", { desc = "Run code block", silent = true, noremap = true })

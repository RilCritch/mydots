return {
  { -- changes color of current line number to match mode colors
    "mawkler/modicator.nvim",
    init = function()
      -- catpuccin integration
      local mocha = require("catppuccin.palettes").get_palette("mocha") -- retrieving catppuccin colors

      -- setting highlights that modicator uses
      vim.api.nvim_set_hl(0, "NormalMode", { fg = mocha.blue })
      vim.api.nvim_set_hl(0, "InsertMode", { fg = mocha.green })
      vim.api.nvim_set_hl(0, "VisualMode", { fg = mocha.mauve })
      vim.api.nvim_set_hl(0, "CommandMode", { fg = mocha.peach })
      vim.api.nvim_set_hl(0, "ReplaceMode", { fg = mocha.red })
      vim.api.nvim_set_hl(0, "SelectMode", { fg = mocha.blue })
      vim.api.nvim_set_hl(0, "TerminalMode", { fg = mocha.blue })
      vim.api.nvim_set_hl(0, "TerminalNormalMode", { fg = mocha.blue })

      -- and defualt number for current line
      vim.api.nvim_set_hl(0, "CursorLineNr", { fg = mocha.blue })
    end,
    config = function()
      require("modicator").setup()
    end,
  },

  { -- making delimiters easier to distinguish
    "HiPhish/rainbow-delimiters.nvim",
    -- extra configuration here if needed
  },
}

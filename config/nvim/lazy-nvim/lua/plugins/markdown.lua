return {
  { -- evaluate code in markdown, orgmode.nvim and norg
    "jubnzv/mdeval.nvim",
  },

  -- { -- Generate md table of contents
  --   -- look into this plugin further
  --   "richardbizik/nvim-toc",
  --   config = function()
  --     require("nvim-toc").setup({})
  --   end,
  -- },

  { -- opens links to other md files in a new buffer using the enter key
    "jghauser/follow-md-links.nvim",
  },

  {
    "lukas-reineke/headlines.nvim",
    dependencies = "nvim-treesitter/nvim-treesitter",
    config = true, -- or `opts = {}`
  },
}

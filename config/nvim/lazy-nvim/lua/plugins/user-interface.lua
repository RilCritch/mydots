return {
  {
    "stevearc/aerial.nvim",
    opts = {},
    -- Optional dependencies
    dependencies = {
      "nvim-treesitter/nvim-treesitter",
      "nvim-tree/nvim-web-devicons",
    },
  },

  -- { -- needs a newer version of neovim unfortunately
  --   "lewis6991/satellite.nvim",
  --   config = function()
  --     require("satellite").setup()
  --   end,
  -- },
}

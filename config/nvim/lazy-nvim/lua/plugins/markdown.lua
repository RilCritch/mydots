return {
  -- ** read documentation to figure out how to use
  -- { -- view markdown as a mindmap (must have yarn installed on system)
  --   "Zeioth/markmap.nvim",
  --   build = "yarn global add markmap-cli",
  --   cmd = { "MarkmapOpen", "MarkmapSave", "MarkmapWatch", "MarkmapWatchStop" },
  --   opts = {
  --     html_output = "/tmp/markmap.html", -- (default) Setting a empty string "" here means: [Current buffer path].html
  --     hide_toolbar = false, -- (default)
  --     grace_period = 3600000, -- (default) Stops markmap watch after 60 minutes. Set it to 0 to disable the grace_period.
  --   },
  --   config = function(_, opts)
  --     require("markmap").setup(opts)
  --   end,
  -- },

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
}

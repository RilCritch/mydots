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
    config = function()
      -- highlights
      local hl = vim.api.nvim_set_hl

      -- headlines
      hl(0, "Headline1", { bold = true, bg = "#392939" })
      hl(0, "Headline2", { bold = true, bg = "#3a2f34" })
      hl(0, "Headline3", { bold = true, bg = "#3a363a" })
      hl(0, "Headline4", { bold = true, bg = "#34413e" })
      hl(0, "Headline5", { bold = true, bg = "#343f5a" })
      hl(0, "Headline6", { bold = true, bg = "#373950" })

      --codeblok

      require("headlines").setup({
        markdown = {
          headline_highlights = {
            "Headline1",
            "Headline2",
            "Headline3",
            "Headline4",
            "Headline5",
            "Headline6",
          },
          codeblock_highlight = "CodeBlock",
          dash_highlight = "Dash",
          dash_string = "-",
          quote_highlight = "Quote",
          quote_string = "┃",
          fat_headlines = true,
          -- fat_headline_upper_string = "▃",
          -- fat_headline_lower_string = "🬂",
          fat_headline_upper_string = "",
          fat_headline_lower_string = "-",
        },
      })
    end,
  },
}

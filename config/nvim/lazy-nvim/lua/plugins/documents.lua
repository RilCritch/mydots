return {
  { -- evaluate code in markdown, orgmode.nvim and norg
    "jubnzv/mdeval.nvim",
  },

  { -- opens links to other md files in a new buffer using the enter key
    "jghauser/follow-md-links.nvim",
  },

  {
    "nvim-neorg/neorg",
    build = ":Neorg sync-parsers",
    dependencies = { "nvim-lua/plenary.nvim" },
    config = function()
      require("neorg").setup({
        load = {
          ["core.defaults"] = {}, -- Loads default behaviour
          ["core.concealer"] = {}, -- Adds pretty icons to your documents
          ["core.dirman"] = { -- Manages Neorg workspaces
            config = {
              workspaces = {
                notes = "~/documents/notes",
              },
            },
          },
        },
      })
    end,
  },

  {
    "lukas-reineke/headlines.nvim",
    dependencies = "nvim-treesitter/nvim-treesitter",
    config = function()
      -- highlights
      local theme = require("catppuccin.palettes").get_palette("mocha")
      local hl = vim.api.nvim_set_hl

      -- headlines
      hl(0, "Headline1", { bold = true, fg = theme.red, bg = "#392939" })
      hl(0, "Headline2", { bold = true, fg = theme.peach, bg = "#3a2f34" })
      hl(0, "Headline3", { bold = true, fg = theme.yellow, bg = "#3a363a" })
      hl(0, "Headline4", { bold = true, fg = theme.green, bg = "#34413e" })
      hl(0, "Headline5", { bold = true, fg = theme.blue, bg = "#343f5a" })
      hl(0, "Headline6", { bold = true, fg = theme.lavender, bg = "#373950" })

      -- neorg highlights
      -- headers
      hl(0, "@neorg.headings.1.prefix", { bold = true, fg = theme.red })
      hl(0, "@neorg.headings.2.prefix", { bold = true, fg = theme.peach })
      hl(0, "@neorg.headings.3.prefix", { bold = true, fg = theme.yellow })
      hl(0, "@neorg.headings.4.prefix", { bold = true, fg = theme.green })
      hl(0, "@neorg.headings.5.prefix", { bold = true, fg = theme.blue })
      hl(0, "@neorg.headings.6.prefix", { bold = true, fg = theme.lavender })

      hl(0, "@neorg.headings.1.title", { bold = true, fg = theme.red })
      hl(0, "@neorg.headings.2.title", { bold = true, fg = theme.peach })
      hl(0, "@neorg.headings.3.title", { bold = true, fg = theme.yellow })
      hl(0, "@neorg.headings.4.title", { bold = true, fg = theme.green })
      hl(0, "@neorg.headings.5.title", { bold = true, fg = theme.blue })
      hl(0, "@neorg.headings.6.title", { bold = true, fg = theme.lavender })

      -- heading links
      hl(0, "@neorg.links.location.heading.1.prefix", { fg = theme.red })
      hl(0, "@neorg.links.location.heading.2.prefix", { fg = theme.peach })
      hl(0, "@neorg.links.location.heading.3.prefix", { fg = theme.yellow })
      hl(0, "@neorg.links.location.heading.4.prefix", { fg = theme.green })
      hl(0, "@neorg.links.location.heading.5.prefix", { fg = theme.blue })
      hl(0, "@neorg.links.location.heading.6.prefix", { fg = theme.lavender })

      hl(0, "@neorg.links.location.heading.1", { underline = true, fg = theme.red })
      hl(0, "@neorg.links.location.heading.2", { underline = true, fg = theme.peach })
      hl(0, "@neorg.links.location.heading.3", { underline = true, fg = theme.yellow })
      hl(0, "@neorg.links.location.heading.4", { underline = true, fg = theme.green })
      hl(0, "@neorg.links.location.heading.5", { underline = true, fg = theme.blue })
      hl(0, "@neorg.links.location.heading.6", { underline = true, fg = theme.lavender })

      -- links
      hl(0, "@neorg.links.location.definition", { fg = theme.green })
      hl(0, "@neorg.links.location.footnote", { fg = theme.maroon })
      hl(0, "@neorg.links.location.generic", { underline = true, fg = theme.blue })
      hl(0, "@neorg.links.location.marker", { fg = theme.lavender })
      hl(0, "@neorg.links.location.url", { underline = true, fg = theme.blue })
      hl(0, "@neorg.links.location.description", { underline = true, fg = theme.lavender })
      hl(0, "@neorg.links.location.external_file.prefix", { fg = theme.blue })
      hl(0, "@neorg.links.location.external_file", { underline = true, fg = theme.blue })
      hl(0, "@neorg.links.location.marker.prefix", { fg = theme.subtext1 })
      hl(0, "@neorg.links.file", { fg = theme.lavender })

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
        norg = {
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
          fat_headline_upper_string = "",
          fat_headline_lower_string = "-",
          -- fat_headline_upper_string = "▃",
          -- fat_headline_lower_string = "🬂",
        },
      })
    end,
  },
}

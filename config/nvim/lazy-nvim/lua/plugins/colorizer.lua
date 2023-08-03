return {
  {
    "NvChad/nvim-colorizer.lua",
    -- opts = {
    --
    -- },
    config = function(_, opts)
      require("colorizer").setup(opts)
    end,
  },
}

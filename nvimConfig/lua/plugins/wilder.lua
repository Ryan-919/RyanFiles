return {
    'gelguy/wilder.nvim',
    config = function()
        local wilder = require('wilder')
        wilder.setup({
            modes = {':', '/', '?'},
        })

        -- Define custom highlights based on the Catppuccin theme
        -- local catppuccin_palette = require("catppuccin.palettes").get_palette()

         -- Load Kanagawa color palette
        local kanagawa_colors = require("kanagawa.colors").setup()

        wilder.set_option('renderer', wilder.popupmenu_renderer(
            wilder.popupmenu_border_theme({
                border = 'rounded', -- Rounded border for the popupmenu
                highlights = {
                    border = 'WilderBorder', -- Custom highlight group for the border
                    default = 'WilderDefault', -- Custom highlight group for the text
                },
                highlighter = wilder.basic_highlighter(),
            })
        ))

        -- Define the highlight groups using Catppuccin colors
        -- vim.api.nvim_set_hl(0, 'WilderBorder', { fg = catppuccin_palette.blue })
        -- vim.api.nvim_set_hl(0, 'WilderDefault', { fg = catppuccin_palette.text, bg = catppuccin_palette.surface0 })

        -- Define highlight groups using Kanagawa colors
        vim.api.nvim_set_hl(0, 'WilderBorder', { fg = kanagawa_colors.waveBlue2 })
        vim.api.nvim_set_hl(0, 'WilderDefault', { fg = kanagawa_colors.fujiWhite, bg = kanagawa_colors.sumiInk1 })


        -- Define key mappings for navigation
        vim.api.nvim_set_keymap('c', '<Tab>', [[wilder#in_context() ? wilder#next() : '<Tab>']], { expr = true, noremap = true })
        vim.api.nvim_set_keymap('c', '<S-Tab>', [[wilder#in_context() ? wilder#previous() : '<S-Tab>']], { expr = true, noremap = true })
    end,
}


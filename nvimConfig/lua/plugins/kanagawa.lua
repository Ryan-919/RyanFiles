return {
    "rebelot/kanagawa.nvim",
    config = function()
        require("kanagawa").setup({
            compile = false, -- Set to true for performance (generates a compiled theme file)
            undercurl = true, -- Enables undercurl for diagnostics
            commentStyle = { italic = true },
            functionStyle = {},
            keywordStyle = { italic = true },
            statementStyle = { bold = true },
            typeStyle = {},
            transparent = false, -- Set to true for a transparent background
            dimInactive = false, -- Dim inactive windows
            terminalColors = true, -- Use Kanagawa colors in the terminal

            colors = {
                theme = {
                    all = {
                        ui = {
                            float = "none", -- Prevents overwriting popup background
                        },
                    },
                },
            },

            overrides = function(colors)
                local theme = colors.theme
                return {
                    -- Custom Wilder highlights
                    WilderBorder = { fg = colors.palette.waveBlue2 },
                    WilderDefault = { fg = colors.palette.fujiWhite, bg = colors.palette.sumiInk1 },

                    -- Borderless Telescope
                    -- TelescopeTitle = { fg = theme.ui.special, bold = true },
                    -- TelescopePromptNormal = { bg = theme.ui.bg_p1 },
                    -- TelescopePromptBorder = { fg = theme.ui.bg_p1, bg = theme.ui.bg_p1 },
                    -- TelescopeResultsNormal = { fg = theme.ui.fg_dim, bg = theme.ui.bg_m1 },
                    -- TelescopeResultsBorder = { fg = theme.ui.bg_m1, bg = theme.ui.bg_m1 },
                    -- TelescopePreviewNormal = { bg = theme.ui.bg_dim },
                    -- TelescopePreviewBorder = { bg = theme.ui.bg_dim, fg = theme.ui.bg_dim },
                }
            end,
        })

        -- Apply the colorscheme
        vim.cmd("colorscheme kanagawa-wave")
    end,
}


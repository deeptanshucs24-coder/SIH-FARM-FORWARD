/* Tailwind design tokens — must run synchronously before body paints */
tailwind.config = {
  darkMode: "class",
  theme: { extend: {
    colors: {
      "surface":"#f7f9ff","surface-dim":"#d7dadf","background":"#f7f9ff",
      "primary-fixed-dim":"#a5d0b9","error-container":"#ffdad6","secondary":"#4c6452",
      "on-tertiary-fixed":"#002114","on-primary":"#ffffff","outline-variant":"#c1c8c2",
      "secondary-fixed-dim":"#b3cdb7","inverse-surface":"#2d3135","primary-container":"#1b4332",
      "primary-fixed":"#c1ecd4","on-error-container":"#93000a","on-secondary":"#ffffff",
      "inverse-primary":"#a5d0b9","on-tertiary-fixed-variant":"#0e5138",
      "tertiary-container":"#00452e","on-primary-fixed-variant":"#274e3d",
      "surface-container-highest":"#e0e3e8","surface-bright":"#f7f9ff",
      "surface-variant":"#e0e3e8","on-tertiary":"#ffffff","error":"#ba1a1a",
      "on-background":"#181c20","surface-container-low":"#f1f4f9","tertiary":"#002d1c",
      "on-surface":"#181c20","primary":"#012d1d","on-secondary-fixed":"#092012",
      "surface-container-lowest":"#ffffff","outline":"#717973","tertiary-fixed":"#b1f0ce",
      "on-primary-container":"#86af99","surface-container":"#ebeef3",
      "on-surface-variant":"#414844","surface-container-high":"#e5e8ee",
      "on-secondary-fixed-variant":"#354c3b","on-secondary-container":"#506856",
      "tertiary-fixed-dim":"#95d4b3","on-tertiary-container":"#75b393",
      "secondary-fixed":"#cee9d3","secondary-container":"#cce6d0",
      "on-primary-fixed":"#002114","surface-tint":"#3f6653","on-error":"#ffffff",
      "inverse-on-surface":"#eef1f6"
    },
    borderRadius: {"DEFAULT":"0.125rem","lg":"0.25rem","xl":"0.5rem","full":"0.75rem"},
    spacing: {"xl":"32px","sm":"8px","margin":"32px","xs":"4px","gutter":"24px","lg":"24px","2xl":"48px","md":"16px","base":"8px","3xl":"64px"},
    fontFamily: {"body-lg":["Inter"],"headline-lg":["Inter"],"body-md":["Inter"],"headline-lg-mobile":["Inter"],"body-sm":["Inter"],"headline-md":["Inter"],"headline-xl-mobile":["Inter"],"headline-xl":["Inter"],"label-md":["Inter"]},
    fontSize: {
      "body-lg":["18px",{lineHeight:"28px",fontWeight:"400"}],
      "headline-lg":["28px",{lineHeight:"36px",letterSpacing:"-0.01em",fontWeight:"600"}],
      "body-md":["16px",{lineHeight:"24px",fontWeight:"400"}],
      "headline-lg-mobile":["24px",{lineHeight:"32px",fontWeight:"600"}],
      "body-sm":["14px",{lineHeight:"20px",fontWeight:"400"}],
      "headline-md":["20px",{lineHeight:"28px",fontWeight:"600"}],
      "headline-xl-mobile":["30px",{lineHeight:"38px",fontWeight:"700"}],
      "headline-xl":["36px",{lineHeight:"44px",letterSpacing:"-0.02em",fontWeight:"700"}],
      "label-md":["12px",{lineHeight:"16px",letterSpacing:"0.05em",fontWeight:"600"}]
    }
  }}
};

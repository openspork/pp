# pp
pp is a WIP Polycom Provisioning webapp that allows webapp GUI-based generation of Polycom phone configs.

## features
- In-flight phone config generation.
- Group-based inheritance -- config applied to parent groups is inherited by children.
- Resultant set of policy (RSoP) accountability -- ability to understand exactly how config inherited by children is inherited.
- Tracks overrides / conflicts between different parents (part of RSoP summary).
- Groups can be assigned certificate authorities (which inherit, like all group parameters).
- Inherited certificate authorities are used to create + apply client certificates to connecting phones.

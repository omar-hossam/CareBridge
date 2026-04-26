export const getNavbar = (req, res) => {
  const user = req.session?.user;

  if (user) {
    return res.send(`
      <a href="/profile" title="${user.name}">
        <img src="/icons/user.svg" width="32" />
      </a>
    `);
  }

  return res.send(`
    <a role="button" href="/login">
      Login <img src="/icons/user.svg" />
    </a>
  `);
};
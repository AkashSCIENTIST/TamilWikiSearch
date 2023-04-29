import React from "react";
import logo from "/tw.svg";

const Sidebar = () => {
  const data = [
    {
      heading: "தமிழ்",
      hyperlinks: [
        {
          name: "முகப்பு - தமிழ்",
          href: "https://tamil.wiki/wiki/%E0%AE%A4%E0%AE%AE%E0%AE%BF%E0%AE%B4%E0%AF%8D_%E0%AE%B5%E0%AE%BF%E0%AE%95%E0%AF%8D%E0%AE%95%E0%AE%BF",
        },
        {
          name: "தமிழ் பக்கங்கள்",
          href: "https://tamil.wiki/wiki/Category:Finalised",
        },
        {
          name: "தொடர்புக்கு",
          href: "https://tamil.wiki/wiki/Tamil_Wiki:%E0%AE%A4%E0%AF%8A%E0%AE%9F%E0%AE%B0%E0%AF%8D%E0%AE%AA%E0%AF%81%E0%AE%95%E0%AF%8D%E0%AE%95%E0%AF%81",
        },
      ],
    },
    {
      heading: "English",
      hyperlinks: [
        {
          name: "Home - English",
          href: "https://tamil.wiki/wiki/Main_Page_(English)",
        },
        {
          name: "English Pages",
          href: "https://tamil.wiki/wiki/Category:Finalised_En",
        },
        {
          name: "Contact",
          href: "https://tamil.wiki/wiki/Tamil_Wiki:Contact",
        },
      ],
    },
    {
      heading: "Tracking",
      hyperlinks: [
        {
          name: "Recent Discussions",
          href: "https://tamil.wiki/wiki/Main_Page_(English)",
        },
        {
          name: "Recent Page Changes",
          href: "https://tamil.wiki/wiki/Category:Finalised_En",
        },
      ],
    },
    {
      heading: "For registered users",
      hyperlinks: [
        {
          name: "செயல்முறை",
          href: "https://tamil.wiki/wiki/Tamil_Wiki:%E0%AE%9A%E0%AF%86%E0%AE%AF%E0%AE%B2%E0%AF%8D%E0%AE%AE%E0%AF%81%E0%AE%B1%E0%AF%88",
        },
        {
          name: "தமிழ் பக்கங்கள் பட்டியல்",
          href: "https://tamil.wiki/wiki/Category:Tamil_Content",
        },
        {
          name: "List of English pages",
          href: "https://tamil.wiki/wiki/Category:English_Content",
        },
      ],
    },
    {
      heading: "Wiki tools",
      hyperlinks: [
        {
          name: "Special Pages",
          href: "https://tamil.wiki/wiki/Special:SpecialPages",
        },
      ],
    },
    {
      heading: "More",
      hyperlinks: [
        {
          name: "What links here",
          href: "https://tamil.wiki/wiki/Special:WhatLinksHere/Tamil_Wiki:Contact",
        },
        {
          name: "Related changes",
          href: "https://tamil.wiki/wiki/Special:RecentChangesLinked/%E0%AE%A4%E0%AE%AE%E0%AE%BF%E0%AE%B4%E0%AF%8D_%E0%AE%B5%E0%AE%BF%E0%AE%95%E0%AF%8D%E0%AE%95%E0%AE%BF",
        },
        {
          name: "Permanent link",
          href: "https://tamil.wiki/index.php?title=%E0%AE%A4%E0%AE%AE%E0%AE%BF%E0%AE%B4%E0%AF%8D_%E0%AE%B5%E0%AE%BF%E0%AE%95%E0%AF%8D%E0%AE%95%E0%AE%BF&oldid=93233",
        },
        {
          name: "Page information",
          href: "https://tamil.wiki/index.php?title=%E0%AE%A4%E0%AE%AE%E0%AE%BF%E0%AE%B4%E0%AF%8D_%E0%AE%B5%E0%AE%BF%E0%AE%95%E0%AF%8D%E0%AE%95%E0%AE%BF&action=info",
        },
        {
          name: "Page logs",
          href: "https://tamil.wiki/index.php?title=Special:Log&page=%E0%AE%A4%E0%AE%AE%E0%AE%BF%E0%AE%B4%E0%AF%8D+%E0%AE%B5%E0%AE%BF%E0%AE%95%E0%AF%8D%E0%AE%95%E0%AE%BF",
        },
      ],
    },
  ];
  return (
    <div className="sidebar-main">
      <img src={logo} alt="" className="tw-logo" />
      {data.map((arr) => (
        <div className="sidebar">
          <p>{arr.heading}</p>
          <hr />
          {arr.hyperlinks.map(({ name, href }) => (
            <li>
              <a href={href} target="_blank">
                {name}
              </a>
            </li>
          ))}
        </div>
      ))}
    </div>
  );
};

export default Sidebar;
